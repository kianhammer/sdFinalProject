from flask import Flask
from flask import render_template
import psycopg2
import json

app = Flask(__name__)

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
def gameStats():
	conn = psycopg2.connect(
		host="localhost",
		port=5432,
		database="chend2",
		user="chend2",
		password="plad242books")

	cur = conn.cursor()

	sql_all_points = """SELECT * FROM cutstats ORDER BY Date DESC;"""
	cur.execute(sql_all_points)
	all_opponents = cur.fetchall()

	all_opponents_html = gameStatsGenerateDropdown(all_opponents)
	
	return render_template("gamestats.html", DropdownOptions = all_opponents_html)

def gameStatsGenerateDropdown(all_opponents):
	opponents = []
	all_opponents_html = ""
	all_opponents_html = all_opponents_html + f'<option value="Select A Game:">Select A Game:</option>'
	all_opponents_html = all_opponents_html + '/n'
	
	for point in all_opponents:

		#point[1] is the opponent of that point
		checkOpponent = point[1]
		
		for opponent in opponents:
			if checkOpponent == opponent:
				checkOpponent = "null"
		
		if checkOpponent != "null":
			opponents.append(checkOpponent)
			all_opponents_html = all_opponents_html + f'<option value="{checkOpponent}">{checkOpponent}</option>'
			all_opponents_html = all_opponents_html + '/n'
	
	return all_opponents_html
	

@app.route('/stats/game/<opponent>')
def gameStatsOpponent(opponent):

	if opponent == "Select A Game:":
		return

	
	conn = psycopg2.connect(
	host="localhost",
	port=5432,
	database="chend2",
	user="chend2",
	password="plad242books")

	cur = conn.cursor()

	sql_game_points = """SELECT * FROM cutstats WHERE Opponent = %s ORDER BY Point DESC;"""
	cur.execute(sql_game_points, [opponent])
	game_points = cur.fetchall()

	score = ""
	for point in game_points:
		score = point[2]


	json_answer = {
        	"score": score
        }
	return json.dumps(json_answer)

if __name__ == '__main__':
	my_port = 5202
	app.run(host='0.0.0.0', port = my_port) 
