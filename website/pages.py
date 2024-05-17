from flask import Flask
from flask import render_template
import random

app = Flask(__name__)

@app.route('/')
def welcome():
    message = f"CUT stats web page" 
    return render_template("homepage.html", someText = message)

@app.route('/stats/players')
def player_stats():
    return render_template("playerStats.html", table = get_player_stats())

def get_player_stats():
    table_html = """<tr>
    <th>Company</th>
    <th>Contact</th>
    <th>Country</th>
  </tr>
  <tr>
    <td>Alfreds Futterkiste</td>
    <td>Maria Anders</td>
    <td>Germany</td>
  </tr>
  <tr>
    <td>Centro comercial Moctezuma</td>
    <td>Francisco Chang</td>
    <td>Mexico</td>
  </tr>"""
    return table_html

if __name__ == '__main__':
    my_port = 5202
    app.run(host='0.0.0.0', port = my_port) 