import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # POST: insert inputted birthday into database
        db.execute("INSERT INTO birthdays (name, day, month) VALUES (?, ?, ?)", request.form.get("name"), request.form.get("day"), request.form.get("month"))

        # refresh page
        return redirect("/")

    else:
        # GET: retrieve birthdays from database
        bdays = db.execute("SELECT name, month, day FROM birthdays;")

        # pass list of dictionaries from database into index.html
        return render_template("index.html", bdays=bdays)