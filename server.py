<<<<<<< HEAD
=======
# from dotenv import load_dotenv, find_dotenv
# load_dotenv(find_dotenv())
>>>>>>> f8b39d7bec836bb3b0261c1753f4d8cd169c3db6
from flask import Flask, render_template, redirect, request, session, flash, jsonify
import pg, os
from time import time
import datetime
from datetime import timedelta

tmp_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask('GBroker', static_url_path = '')
db = pg.DB(
   dbname=os.environ.get('PG_DBNAME'),
   host=os.environ.get('PG_HOST'),
   user=os.environ.get('PG_USERNAME'),
   passwd=os.environ.get('PG_PASSWORD')
)

#Route to main
@app.route('/')
def route_index():
    return app.send_static_file('index.html');

<<<<<<< HEAD
=======
@app.route('/home')
def home():
    return 'Tits';

>>>>>>> f8b39d7bec836bb3b0261c1753f4d8cd169c3db6
app.run(debug=True)
