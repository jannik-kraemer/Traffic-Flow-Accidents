from flask import Flask, render_template
import datetime

app = Flask('Interface')

def getTest():
    return datetime.datetime.now()

dynamic = getTest()

@app.route('/')
def index():
    return render_template('index.html', variable=dynamic)
