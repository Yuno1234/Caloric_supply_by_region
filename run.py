from flask import Flask
app = Flask(__name__)

# env\Scripts\activate.bat
# pip install flask
# set FLASK_APP=run.py
# set FLASK_DEBUG=1
# py -m flask run

@app.route('/')
def index():
    return('<h1>hello world</h1>')