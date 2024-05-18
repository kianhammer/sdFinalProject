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
    stats = fetch_player_stats()
    print("stats = " + stats)
    return render_template("playerStats.html", stats=stats)

#This fetches a table of data
@app.route('/stats/fetch')
def fetch_player_stats():
    
    # cur.execute("""SELECT * FROM cutstats""")
    # all_stats = cur.fetchall()

    players_list = get_all_players()
    print('players = '+ str(players_list))

    all_player_stats = [] # maybe add column headers?

    for player in players_list:
        all_player_stats.append(calc_player_stats(player))

    # data = {"data": all_player_stats}
    # print("data: " + str(data))

    # #json.dumps creates a json object
    # return json.dumps(data)

    return json.dumps(all_player_stats)


def get_all_players():
    player_list = []

    cur.execute("SELECT players FROM cutstats")
    result = cur.fetchall()
    for point in result:
        for player in point[0].split("|"):
            if player not in player_list:
                player_list.append(player)
    return player_list



# makes a dictionary of the player's stats
def calc_player_stats(player):

    stats = [player]

    stats.append(query(f"SELECT COUNT(*) FROM cutstats WHERE players LIKE '%{player}%';"))
    
    stats.append(query(f"SELECT COUNT(*) FROM cutstats WHERE Players LIKE '%{player}%' AND SCORED LIKE 'TRUE' AND Pulled LIKE 'FALSE';"))

    return stats

#queries the sql database with the given command
def query(sql):
    cur.execute(sql)
    result = cur.fetchone()
    if result == None:
        return result
    else:
        return result[0]


if __name__ == '__main__':
    my_port = 5202
    app.run(host='0.0.0.0', port = my_port) 