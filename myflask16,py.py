#!/usr/bin/python3

import datetime
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def welcome():
    names_of_instructors = ["Zach Feeser", "Ed Choe", "Dave Egan"]
    random_name = "Jose"
    return render_template('hellobasic.html', names=names_of_instructors, name=random_name)

@app.route('/adv/<name>')
def adv(name):
    now = datetime.datetime.now()
    jt = now.hour

    return render_template("helloadv.html", joevar = name, jt = jt)

if __name__ == "__main__":
    app.run(port=5006)
