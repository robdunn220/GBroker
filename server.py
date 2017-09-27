from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
from flask import Flask, render_template, redirect, request, session, flash, jsonify
import pg, os
from time import time
import datetime
from datetime import timedelta

tmp_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Images')
app = Flask('GBroker', static_url_path = '')
db = pg.DB(
   dbname=os.environ.get('PG_DBNAME'),
   host=os.environ.get('PG_HOST'),
   user=os.environ.get('PG_USERNAME'),
   passwd=os.environ.get('PG_PASSWORD')
)

print(os.environ.get('PG_HOST'))

#Route to main
@app.route('/')
def route_index():
    return app.send_static_file('index.html');

@app.route('/home')
def home():
    return 'F';

@app.route('/guns')
def guns():
    result = db.query('Select * from handguns')
    data = result.dictresult()
    return jsonify(data);

app.run(debug=True)
