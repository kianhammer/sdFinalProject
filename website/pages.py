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
    "Huck Attempts": "SELECT SUM(HucksCompleted) + SUM(HucksIncompleteForced) + SUM(HucksIncompleteUnforced) + SUM(HucksIncompleteUnknown) FROM cutstats WHERE players LIKE '%player%';",
    "Huck Completed": "SELECT SUM(HucksCompleted) FROM cutstats WHERE players LIKE '%player%';",
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

@app.route('/stats/game/<opponent>')
def gameStats(opponent):
	
	conn = psycopg2.connect(
	host="localhost",
	port=5432,
	database="chend2",
	user="chend2",
	password="plad242books")

	cur = conn.cursor()

	sql_game_points = """SELECT * FROM cutstats WHERE Opponent = %s ORDER BY Point DESC;"""
	cur.execute(sql_game_points, opponent)
	cornellHucks = cur.fetchall()
	return render_template("homepage.html", someText = f"hello")

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
