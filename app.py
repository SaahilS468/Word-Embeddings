from flask import Flask, render_template, request, redirect, url_for
from recom import Recom
app = Flask(__name__)

# l = ["Topic 1","Topic 2","Topic 3","Topic 4","Topic 5","Topic 6","Topic 7","Topic 8","Topic 9","Topic 10"]

@app.route("/", methods = ["GET","POST"])
def home():
    if request.method == "POST":
        topic = request.form['name']
        model = Recom(topic)
        sim = model.find_sim()
        return render_template('home.html',topics=sim)
    else:
        sim = []
        return render_template('home.html', topics=sim)