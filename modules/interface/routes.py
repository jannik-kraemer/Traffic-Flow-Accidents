from flask import Flask, render_template

@app.route("/")
def index():
    return render_template('index.html', variable=dynamic)
