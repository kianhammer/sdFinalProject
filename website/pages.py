from flask import Flask
from flask import render_template
import random
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

@app.route('/')
def welcome():
    message = f"CUT stats web page" 
    return render_template("homepage.html", someText = message)

@app.route('/stats/players')
def player_stats():
    return render_template("playerStats.html")

#This fetches a table of data
@app.route('/stats/fetch/<player>')
def fetch_player_stats(player):
    
    # cur.execute("""SELECT * FROM cutstats""")
    # all_stats = cur.fetchall()

    json_answer = calc_player_stats(player)

    # json_answer = {
    #     "origin": "fetch_number",
    #     "name":  name,
    #     "value":  answer
    #     }

    #json.dumps creates a json object
    return json.dumps(json_answer)


# makes a dictionary of the player's stats
def calc_player_stats(player):
    stats = {"player": player}

    stats["points"] = query(f"SELECT COUNT(*) FROM cutstats WHERE players LIKE '%{player}%';")

    stats["holds"] = query(f"SELECT COUNT(*) FROM cutstats WHERE Players LIKE '%{player}%' AND SCORED LIKE 'TRUE' AND Pulled LIKE 'FALSE';")

    print(stats)

    return stats

#queries the sql database with the given command
def query(sql):
    cur.execute(sql)
    result = cur.fetchone()
    print(result)
    if result == None:
        return result
    else:
        return result[0]


if __name__ == '__main__':
    my_port = 5202
    app.run(host='0.0.0.0', port = my_port) 