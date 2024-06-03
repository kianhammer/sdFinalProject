from flask import Flask, request, jsonify
from flask import render_template
import psycopg2
import json
import os
import csv 

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="chend2",
    user="chend2",
    password="plad242books")
    
cur = conn.cursor()

all_cut_games = []

PLAYER_STATS_QUERIES = {
    "PP": "SELECT COUNT(*)",
    "OPP": "SELECT COUNT(*) FILTER (WHERE pulled LIKE 'FALSE')",
    "DPP": "SELECT COUNT(*) FILTER (WHERE pulled LIKE 'TRUE')",
    "Holds": "SELECT COUNT(*) FILTER (WHERE scored LIKE 'TRUE' AND pulled LIKE 'FALSE')",
    "Hold %" : "SELECT ROUND(CAST(COUNT(*) FILTER (WHERE scored LIKE 'TRUE' AND pulled LIKE 'FALSE') AS FLOAT) / NULLIF(COUNT(*) FILTER (WHERE pulled LIKE 'FALSE'), 0), 2)",
    "Breaks": "SELECT COUNT(*) FILTER (WHERE scored LIKE 'TRUE' AND pulled LIKE 'TRUE')",
    "Break %" : "SELECT CAST(COUNT(*) FILTER (WHERE scored LIKE 'TRUE' AND pulled LIKE 'TRUE') AS FLOAT) / NULLIF(COUNT(*) FILTER (WHERE pulled LIKE 'TRUE'), 0)",
    "RZ Attempts": "SELECT SUM(EndzoneScored) + SUM(EndzoneNotScoredForced) + SUM(EndzoneNotScoredUnforced) + SUM(EndzoneNotScoredUnknown)",
    "RZC %": "SELECT SUM(EndzoneScored) / NULLIF((SUM(EndzoneScored) + SUM(EndzoneNotScoredForced) + SUM(EndzoneNotScoredUnforced) + SUM(EndzoneNotScoredUnknown)), 0)",
    "Turns": "SELECT SUM(TurnoversForced) + SUM(TurnoversUnforced)",
    "Turns/PP": "SELECT (SUM(TurnoversForced) + SUM(TurnoversUnforced)) / COUNT(*)",
    "Blocks": "SELECT SUM(BlocksForced) + SUM(BlocksUnforced)",
    "Huck Attempts": "SELECT SUM(HucksCompleted) + SUM(HucksIncompleteForced) + SUM(HucksIncompleteUnforced) + SUM(HucksIncompleteOther)",
    "Huck %": "SELECT SUM(HucksCompleted) / NULLIF((SUM(HucksCompleted) + SUM(HucksIncompleteForced) + SUM(HucksIncompleteUnforced) + SUM(HucksIncompleteOther)), 0)",
    "OEFF": "SELECT (COUNT(*) FILTER (WHERE scored LIKE 'TRUE')) / NULLIF((SUM(BlocksForced) + SUM(BlocksUnforced) + COUNT(*) FILTER (WHERE pulled LIKE 'FALSE')), 0)",
}
PLAYER_STATS_CATEGORIES = {
    "Points Played": "Points in which the player has been on the field",
    "Offensive Points Played": "Points in which the player was on the field while starting on offense",
    "Defensive Points Played": "Points in which the player was on the field while starting on defense",
    "Holds": "When a player is on the field for an Offensive Point and his team scores",
    "Hold %": "holds/offensive points",
    "Breaks": "When a player is on the field for a Defensive Point and his team scores",
    "Break %": "breaks/defensive points",
    "Red Zone Attempts": "Possessions when the disc is within 20 yards of the end zone",
    "Red Zone Conversion %": "Rate of success on possessions when the disc is withing 20 yards of the end zone",
    "Turnovers": "When a player is on the field and his team loses possession of the disc",
    "Turnovers Per Point Played": "Average turnovers per point in which the player was on the field",
    "Blocks": "When a player is on the field and his team takes possession away from the other team",
    "Huck Attempts": "When a player is on the field while his team attempts a throw of more than 40 yards",
    "Huck Completion %": "Rate of completed hucks per attempt while on the field",
    "Offensive Efficiency": "Scores / possessions while a player is on the field",
}

@app.route('/')
def welcome():
    rows = query_fetch_all("SELECT Opponent FROM CUTStats")
    
    gameset = set(rows)
    
    return render_template("homepage.html", gamenumber = len(gameset))

@app.route('/import/')
def importpage():
	return render_template("importgame.html")

@app.route('/api', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return render_template("upload_error.html", message = 'File upload error')

    file = request.files['file']

    if file.filename == '':
        return render_template("upload_error.html", message = 'File not found')

    if file.filename[-4:] != '.csv':
        return render_template("upload_error.html", message = 'File must be a csv')

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    with open(filepath, newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = [row for row in reader]

	# The data from an entry csv must be in a very specific format in order to enter it into the table. This is the
	# reason for all of the seemingly arbitrary indices in the following sql insert statement. The following loops
	# through each point in a given game's csv and takes the appropriate data entry for each column, then writing
	# that data into the table.
    score = f"{data[2][0]} - {data[2][1]}"
    for i in range(1, len(data[3])):
        sql = f"INSERT INTO CUTStats VALUES ('{data[0][1]}', '{data[1][1]}', '{score}', {data[3][i]}, '{data[4][i].upper()}', '{data[5][i].upper()}', {data[6][i]}, {data[7][i]}, {data[8][i]}, {data[9][i]}, {data[10][i]}, {data[11][i]}, {data[12][i]}, {data[13][i]}, {data[14][i]}, {data[15][i]}, {data[16][i]}, {data[17][i]}, '{data[18][i]}')"
        cur.execute( sql )
        conn.commit()

    return render_template("upload_success.html", opponent = data[1][1])

@app.route('/stats/game')
def game_stats():
	all_points = query_fetch_all("""SELECT * FROM cutstats ORDER BY Date DESC;""")
	separate_games(all_points)
	all_opponents_html = game_stats_generate_dropdown()
	
	return render_template("gamestats.html", DropdownOptions = all_opponents_html)

#makes a separate list entry in all_cut_games of every game, each game entry consists of a list of the points of that game
def separate_games(all_points):
	game = []
	previous_point = []
	
	for point in all_points:	
		if not game:
			game.append(point)
		else:
			#check if each sequential point is of the same game as the previous point
			if previous_point[1] == point[1] and get_timestamp_date(previous_point[0]) == get_timestamp_date(point[0]):
				game.append(point)
			else:
				all_cut_games.append(game)
				game = []
		previous_point = point
	
	#appends the points of the most recent game listed in the database	
	all_cut_games.append(game)

def get_timestamp_date(timestamp):
	return str(timestamp)[0:10]
			
def game_stats_generate_dropdown():
	all_opponents_html = ""
	all_opponents_html = all_opponents_html + f'<option value="Select A Game:">Select A Game:</option>' + '/n'
	
	#index i put in the value of the dropdown menu, so that the index of the game can be accessed easily later
	i = 0
	for game in all_cut_games:
		opponent = game[0][1]
		all_opponents_html = all_opponents_html + f'<option value="{i} {opponent}">{opponent}</option>' + '/n'
		i += 1
		
	return all_opponents_html
	

@app.route('/stats/game/<opponent>')
def game_stats_opponent(opponent):

	if opponent == "Select A Game:":
		return

	#retrieves the points of the game selected by the user
	opponent_index = int(opponent[0:1])
	game_points = all_cut_games[opponent_index]

	score = ""
	for point in game_points:
		score = point[2]

	json_answer = {
        	"score": score
        }
	return json.dumps(json_answer)


@app.route('/stats/players')
def player_stats_page():
    player_stats = fetch_player_stats()
    tooltips = json.dumps(PLAYER_STATS_CATEGORIES)
    stats_categories = json.dumps(list(PLAYER_STATS_QUERIES.keys()))
    return render_template("playerstats.html", tooltips=tooltips, statCategories=stats_categories, stats=player_stats)

def fetch_player_stats():
    all_player_stats = {}

    for player in get_all_players():
        all_player_stats[player] = calc_player_stats(player)

    return json.dumps(all_player_stats)


def get_all_players():
    player_list = []

    for point in query_fetch_all("SELECT players FROM cutstats"):
        for player in point[0].split("|"): # players are in the format "player1|player2|player3|..."
            if player not in player_list:
                player_list.append(player)
                
    return player_list


def calc_player_stats(player):

    stats = [player]

    for category in PLAYER_STATS_QUERIES:
        query = PLAYER_STATS_QUERIES[category] + f" FROM cutstats WHERE players LIKE '%{player}%';"
        stats.append(query_fetch_one(query))

    return stats

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
