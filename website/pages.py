from flask import Flask
from flask import render_template
import random

app = Flask(__name__)

@app.route('/')
def welcome():
    message = f"CUT stats web page" 
    return render_template("homepage.html", someText = message)

if __name__ == '__main__':
    my_port = 5202
    app.run(host='0.0.0.0', port = my_port) 