from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# env\Scripts\activate.bat
# pip install flask
# set FLASK_APP=run.py
# set FLASK_DEBUG=1
# py -m flask run

KCALDB = 'kcal-per-person.db'

def getColor(kcal):
    if kcal > 3500 and kcal < 4000:
        return "#FF0000"
    elif kcal > 3000 and kcal < 3499:
        return "#CC0000"
    elif kcal > 2500 and kcal < 2999:
        return "#990000"
    elif kcal > 2000 and kcal < 2499:
        return "#550000"
    elif kcal > 1500 and kcal < 1999:
        return "#330000"
    elif kcal > 0 and kcal < 1499:
        return "#110000"
    else:
        return "#000000"

country = {}

@app.route('/', methods=['GET', 'POST'])
def index():
  con = sqlite3.connect(KCALDB)
  years = []
  year = 1961
  cur = con.execute('SELECT year FROM food_supply_kcal WHERE entity = "Japan"')
  for row in cur:
    years.append(list(row))

  if request.method == 'POST':
    year = request.form['years']
    print(year)
    cur = con.execute('SELECT entity, kcal FROM food_supply_kcal WHERE year = ?', (year,))
    for row in cur:
      country[row[0]] = getColor(row[1])

  if request.method == 'GET':
    cur = con.execute('SELECT entity, kcal FROM food_supply_kcal WHERE year = "1961"')
    for row in cur:
      country[row[0]] = getColor(row[1])
    



  con.close()
  return render_template('index.html', years=years, country=country, selected=int(year))