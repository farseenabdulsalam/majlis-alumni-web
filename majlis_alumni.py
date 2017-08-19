import os
import psycopg2
from urllib import parse as urlparse
from flask import Flask, render_template, send_from_directory, request, redirect, url_for
app = Flask(__name__)

def connect_db():
    """Connects to the specific database."""
    urlparse.uses_netloc.append("postgres")
    url = urlparse.urlparse(os.environ["DATABASE_URL"])
    conn = psycopg2.connect(database=url.path[1:],
                     user=url.username,
                     password=url.password,
                     host=url.hostname, port=url.port ) 
    return conn

@app.route('/')
def home():
    return send_from_directory('.','index.html')

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)


@app.route('/suggest/dates',methods=['POST'])
def suggest_dates():
    if request.method != 'POST' or \
       not request.form['dates']:
        return redirect(url_for('home'))
    conn = connect_db()
    cur = conn.cursor()
    data = (request.form['name'],request.form['year'],request.form['dates'])
    cur.execute('INSERT INTO date_suggestions (name,batch,dates) VALUES (%s,%s,%s)',data)
    conn.commit()
    conn.close()
    return send_from_directory('.','thanks.html')

@app.route('/suggest/programs',methods=['POST'])
def suggest_programs():
    if request.method != 'POST' or \
       not request.form['datas']:
        return redirect(url_for('home'))
    conn = connect_db()
    cur = conn.cursor()
    data = (request.form['name'],request.form['year'],request.form['datas'])
    cur.execute('INSERT INTO programs_suggestions (name,batch,programs) VALUES (%s,%s,%s)',data)
    conn.commit()
    conn.close()
    return send_from_directory('.','thanks.html')

@app.route('/attendance',methods=['POST'])
def attendance():
    if request.method != 'POST' or \
       not request.form['name'] or \
       not request.form['year']:
        return redirect(url_for('home'))
    conn = connect_db()
    cur = conn.cursor()
    data = (request.form['name'],request.form['year'],request.form['okay'])
    cur.execute('INSERT INTO attendance (name,batch,okay) VALUES (%s,%s,%s)',data)
    conn.commit()
    conn.close()
    return send_from_directory('.','thanks.html')

