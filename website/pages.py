from flask import Flask
from flask import render_template
import random

app = Flask(__name__)

@app.route('/')
def welcome():
    message = f"CUT stats web page" 
    return render_template("homepage.html", someText = message)

@app.route('/stats/game/<opponent>')
def gameStats(opponent):
	
	conn = psycopg2.connect(
	host="localhost",
	port=5432,
	database="chend2",
	user="chend2",
	password="plad242books")

	cur = conn.cursor()

  	sql_GamePoints = """SELECT * FROM cutstats WHERE Opponent = %s ORDER BY Point DESC;"""\
	cur.execute(sql_GamePoints)
  	cornellHucks = cur.fetchall()
	return render_template("homepage.html", someText = f"hello")

if __name__ == '__main__':
    my_port = 5202
    app.run(host='0.0.0.0', port = my_port) 
