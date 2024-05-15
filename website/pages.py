from flask import Flask
from flask import render_template
import psycopg2

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

    message = f"CUT stats web page" 
    return render_template("homepage.html", gamenumber = len(gameset))

if __name__ == '__main__':
    my_port = 5202
    app.run(host='0.0.0.0', port = my_port) 