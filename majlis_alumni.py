from flask import Flask, render_template, send_from_directory
app = Flask(__name__)

@app.route('/')
def home():
    return send_from_directory('.','index.html')
