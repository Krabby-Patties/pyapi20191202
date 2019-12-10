#!/usr/bin/python3

import json
import random
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def home():
    return  '''<a href="jays_poems">Grab a random J poem poems</a>
    <p>
    <a href="por,uploader">Upload a Poem</a>'''

@app.route("/jays_poems", defaults={'pn':'batman'})
@app.route("/jays_poems/<pn>")
def send(pn):
    with open('poems.json') as jp:
        jp = json.load(jp)
    if jp.get(pn):
        return jp.get(pn)
    else:
        return "the key does not exist"

@app.route("/poemuploader", methods= ["GET", "POST"])
def poemuploader():
    if request.method == "POST":
        f = request.files['file']
        f =f.read().decode() ## read the new poem out of the uploaded file
        highestkey = pythonpoems.keys()
        pythonpoems[str(int(sorted(highestkey)[-1])+1)] = f
        with open("poems.json", "w") as npj:
            json.dump(pythonpoems, npj)
        return "New poem has been added to the database"
    if request.method == "GET":
    return render_template("upload.html")

if __name__ == '__main__':
    with open("poems.json")