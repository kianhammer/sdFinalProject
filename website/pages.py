from flask import Flask
from flask import render_template
import psycopg2
import json

app = Flask(__name__)

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="chend2",
    user="chend2",
    password="plad242books")
    
cur = conn.cursor()

all_cut_games = []

PLAYER_STATS_QUERIES = {
    "Points": "SELECT COUNT(*) FROM cutstats WHERE players LIKE '%player%';",
    "O Points": "SELECT COUNT(*) FROM cutstats WHERE players LIKE '%player%' AND pulled LIKE 'FALSE';",
    "D Points": "SELECT COUNT(*) FROM cutstats WHERE players LIKE '%player%' AND pulled LIKE 'TRUE';",
    "Holds": "SELECT COUNT(*) FROM cutstats WHERE players LIKE '%player%' AND scored LIKE 'TRUE' AND pulled LIKE 'FALSE';",
    "Breaks": "SELECT COUNT(*) FROM cutstats WHERE players LIKE '%player%' AND scored LIKE 'TRUE' AND pulled LIKE 'TRUE';",
    "EZ Chances": "SELECT SUM(EndzoneScored) + SUM(EndzoneNotScoredForced) + SUM(EndzoneNotScoredUnforced) + SUM(EndzoneNotScoredUnknown) FROM cutstats WHERE players LIKE '%player%';",
    "EZ Scores": "SELECT SUM(EndzoneScored) FROM cutstats WHERE players LIKE '%player%';",
    "Turnovers": "SELECT SUM(TurnoversForced) + SUM(TurnoversUnforced) FROM cutstats WHERE players LIKE '%player%';",
    "Blocks": "SELECT SUM(BlocksForced) + SUM(TurnoversUnforced) FROM cutstats WHERE players LIKE '%player%';",
}



@app.route('/')
def welcome():
	conn = psycopg2.connect(
	host="localhost",
	port=5432,   
	database="chend2",
	user="chend2",
	password="plad242books")

	cur = conn.cursor()

	sql = f"SELECT Opponent FROM CUTStats"
    
	cur.execute( sql )

	rows = cur.fetchall()

	gameset = set(rows)

	return render_template("homepage.html", gamenumber = len(gameset))

@app.route('/import/')
def importpage():
	return render_template("importgame.html")

@app.route('/stats/game')
def game_stats():
	all_points = query_fetch_all("""SELECT * FROM cutstats ORDER BY Date DESC;""")
	separate_games(all_points)
	all_opponents_html = game_stats_generate_dropdown()
	
	return render_template("gamestats.html", DropdownOptions = all_opponents_html)

# Makes a separate list entry in all_cut_games of every game, each game entry consists of a list of the points of that game
def separate_games(all_points):
	game = []
	for point in all_points:
		if not game:
			game.append(point)
		else:
			#if the current point is listed as the first point of the game, the previous points appended to game were all of the previous game
			ifpoint[3] == 1:
				all_cut_games.append(game)
				game = []
				game.append(point)
			else:
				game.append(point)
	
	# Appends the points of the most recent game listed in the database	
	all_cut_games.append(game)
			
def game_stats_generate_dropdown():
	all_opponents_html = ""
	all_opponents_html = all_opponents_html + f'<option value="Select A Game:">Select A Game:</option>' + '/n'
	
	# Index 'i' put in the value of the dropdown menu, so that the index of the game can be accessed easily later
	i = 0
	for game in all_cut_games:
		opponent = game[0][1]
		date = get_timestamp_date(game[0][0])
		all_opponents_html = all_opponents_html + f'<option value="{i} {opponent}">{date} :  {opponent}</option>' + '/n'
		i += 1
		
	return all_opponents_html
	

@app.route('/stats/game/<opponent>')
def game_stats_opponent(opponent):

	if opponent == "Select A Game:":
		return

	# Retrieves the points of the game selected by the user
	opponent_index = int(opponent[0:1])
	game_points = all_cut_games[opponent_index]

	
	cut_breaks = 0
	opp_breaks = 0
	cut_holds = 0
	opp_holds = 0
	
	# List of all the miscellaneous stats that can be tallied
	other_stats_sum = [0,0,0,0,0,0,0,0,0,0,0,0]
	
	for point in game_points:
		#checks to see if the point was a hold or a break, and of what team
		if point[4] == "TRUE":
			if point[5] == "TRUE":
				cut_breaks += 1
			else:
				opp_holds += 1
		else:
			if point[5] == "TRUE":
				cut_holds += 1

			else:
				opp_breaks += 1

		# Tallies to the list of miscellaneous stats
		for i in range(len(other_stats_sum)):
			# The stat values of each point that can be tallied start 6 elements into the point
			other_stats_sum[i] += point[i+6]
				

	json_answer = {
		
        	"score": game_points[0][2],
		"opponent": game_points[0][1],
		"date": get_timestamp_date(game_points[0][0]),
		"cutBreaks": cut_breaks,
		"cutHolds": cut_holds,
		"oppBreaks": opp_breaks,
		"oppHolds": opp_holds,
		"completeHucks": other_stats_sum[0],
		"incompleteHucks": other_stats_sum[1] + other_stats_sum[2] + other_stats_sum[3],
		"endzoneScores": other_stats_sum[4],
		"endzoneNotScores": other_stats_sum[5] + other_stats_sum[6] + other_stats_sum[7],
		"blocksForced": other_stats_sum[8],
		"blocksUnforced": other_stats_sum[9],
		"turnoversForced": other_stats_sum[10],
		"turnoversUnforced": other_stats_sum[11]	
        }
	return json.dumps(json_answer)


@app.route('/stats/players')
def player_stats_page():
    player_stats = fetch_player_stats()
    stats_categories = json.dumps(list(PLAYER_STATS_QUERIES.keys()))
    return render_template("playerStats.html", header=stats_categories, stats=player_stats)

def fetch_player_stats():
    all_player_stats = {}

    for player in get_all_players():
        all_player_stats[player] = calc_player_stats(player)

    return json.dumps(all_player_stats)


def get_all_players():
    player_list = []

    for point in query_fetch_all("SELECT players FROM cutstats"):
        for player in point[0].split("|"):
            if player not in player_list:
                player_list.append(player)
                
    return player_list


def calc_player_stats(player):

    stats = [player]

    for category in PLAYER_STATS_QUERIES:
        stats.append(query_fetch_one(PLAYER_STATS_QUERIES[category].replace("%player%", f"%{player}%")))

    return stats

# Returns the date of an inputted timestamp
def get_timestamp_date(timestamp):
	return str(timestamp)[0:10]

# Query the sql database with the given command
# Returns only the first result
def query_fetch_one(sql):
    cur.execute(sql)
    result = cur.fetchone()
    if result == None:
        return result
    else:
        return result[0]

# Query the sql database with the given command
# Returns all results in a list of tuples - [(result,), (result,)]
def query_fetch_all(sql):
    cur.execute(sql)
    result = cur.fetchall()
    return result


if __name__ == '__main__':
	my_port = 5202
	app.run(host='0.0.0.0', port = my_port) 
