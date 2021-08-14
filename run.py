from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# env\Scripts\activate.bat
# pip install flask
# set FLASK_APP=run.py
# set FLASK_DEBUG=1
# py -m flask run

KCALDB = 'kcal-per-person.db'

# def getColor(kcal):
#     if kcal > 3500 and kcal < 4000:
#         return 
#     elif kcal > 3000 and kcal < 3499:
#         return
#     elif kcal > 2500 and kcal < 2999:
#         return
#     elif kcal > 2000 and kcal < 2499:
#         return
#     elif kcal > 1500 and kcal < 1999:
#         return
#     elif kcal > 0 and kcal < 1499:
#         return
#     else
#         return

country = {
  'Afghanistan': '#FF2211'
}

@app.route('/', methods=['get'])
def index():
  con = sqlite3.connect(KCALDB)
  years = []
  cur = con.execute('SELECT year FROM food_supply_kcal WHERE entity = "Japan"')
  for row in cur:
    years.append(list(row))

  countries = []
  cur = con.execute('SELECT entity, kcal FROM food_supply_kcal WHERE year = "2017"')
  for row in cur:
    year.append(list(row))

  print(request.form)
  con.close()
  return render_template('index.html', years=years, country=country)