import os
import sqlite3
from flask import Flask, render_template, send_from_directory, request
app = Flask(__name__)

# Load default config and override config from an environment variable
app.config.update(dict( DATABASE=os.path.join(app.root_path, 'flaskr.db'),
                       SECRET_KEY='development key', USERNAME='admin',
                       PASSWORD='default'))

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

@app.route('/')
def home():
    return send_from_directory('.','index.html')

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)


@app.route('/suggest/dates')
def suggest_dates():
    if request.method != 'POST' or \
       not request.form['dates']:
        return redirect(url_for('home'))



