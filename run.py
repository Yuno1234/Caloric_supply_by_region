from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# env\Scripts\activate.bat
# pip install flask
# set FLASK_APP=run.py
# set FLASK_DEBUG=1
# py -m flask run

KCALDB = 'kcal-per-person.db'

@app.route('/')
def index():
    con = sqlite3.connect(KCALDB)
    return render_template('index.html')