import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    # create list for dictionaries for each stock
    portfolio = []

    # query database for list of traded stock for user
    tradedstocks = db.execute("SELECT name, symbol, shares FROM transactions WHERE id = ? ORDER BY name", session["user_id"])

    # find amount of cash for user
    cur_money = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0].get("cash")

    # create temp dictionary for stocks & float for total value
    temp = {}
    total = 0

    # add initial name, symbol, amount and price
    try:
        temp.update({"name" : tradedstocks[0]["name"], "symbol" : tradedstocks[0]["symbol"], "shares" : 0, "price" : lookup(tradedstocks[0]["symbol"]).get("price")})
    except:
        # case for when user has no traded stocks
        return render_template("index.html", portfolio=[], cash=usd(cur_money), total=usd(cur_money))

    # iterate over each stock for current amount of stocks
    for transaction in tradedstocks:

        # if new stock is different
        if temp["name"] != transaction["name"]:

            # check if user has any shares -  I would make the whole calculation and reinitialisation proceess in helpers.py
            # into a function to avoid copy paste, but I am not sure if submit50 will take helpers.py as well
            if temp["shares"] != 0:

                # add to total value
                total += temp["shares"] * temp["price"]

                # change price element to formatted string to show
                temp["price"] = usd(temp["price"])

                # add dictionary to portfolio and reset
                portfolio.append(temp)

            temp = {}
            temp.update({"name" : transaction["name"], "symbol" : transaction["symbol"], "shares" : 0, "price" : lookup(transaction["symbol"]).get("price")})

        # calculate amount of stock in portfolio
        temp["shares"] += transaction["shares"]

    # check if any shares for final stock
    if temp["shares"] != 0:
        # add final stock to portfolio
        total += temp["shares"] * temp["price"]
        temp["price"] = usd(temp["price"])
        portfolio.append(temp)

    return render_template("index.html", portfolio=portfolio, cash=usd(cur_money), total=usd(total + cur_money))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    if request.method == 'POST':

        # check if valid number of stocks
        try:
            shares = request.form.get("shares")
            shares = int(shares)
            if shares <= 0:
                return apology("Please input a positive number of shares")
        except:
            return apology("Please input a valid number of shares")

        # check if symbol exists
        stock = lookup(request.form.get("symbol"))
        if stock == None:
            return apology("Please input a valid stock symbol")

        # check if user has enough money
        cur_money = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0].get("cash")
        if stock["price"] * shares > cur_money:
            return apology("Not enough funds")

        # set cash in database to new amount
        cur_money -= stock["price"] * shares
        db.execute("UPDATE users SET cash = ? WHERE id = ?", cur_money, session["user_id"])

        # input new row into transaction table
        db.execute("INSERT INTO transactions (id, name, symbol, price, shares) VALUES (?, ?, ?, ?, ?)", session["user_id"], stock["name"], stock["symbol"], stock["price"], shares)

        return redirect("/")

    else:
        return render_template("buy.html")



@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    # get transaction history from database
    transactions = db.execute("SELECT name, symbol, price, shares, ts FROM transactions WHERE id = ?", session["user_id"])

    # check if buy or sell and add to
    for transaction in transactions:
        if transaction["shares"] > 0:
            transaction.update({"type" : "Buy"})
        else:
            transaction.update({"type" : "Sell"})
            transaction["shares"] = 0 - transaction["shares"]

    return render_template("history.html", transactions=transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password")

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password")

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Searches price of stocks"""

    if request.method == 'POST':

        # look up price of given symbol
        stock = lookup(request.form.get("symbol"))

        # if able to get stock information
        if stock:

            # display to user
            return render_template("/quoted.html", name=stock["name"], price=usd(stock["price"]), symbol=stock["symbol"])
        else:

            # otherwise return apology
            return apology("Error, please double check symbol")
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == 'POST':

        # check if username & password empty
        if not request.form.get("username") or not request.form.get("password"):
            return apology("Please provide a valid username and password")

        # check if passwords match
        if request.form.get("password") != request.form.get("confirmation"):
            return apology("Passwords do not match")

        # otherwise try to enter new user into database
        try:
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", request.form.get("username"), generate_password_hash(request.form.get("password")))
        except:
            # error given if username already in database
            return apology("Username already exists")

        # set cookie so the user is now logged into new account and redirect to homepage
        session["user_id"] = db.execute("SELECT id FROM users WHERE username = ?", request.form.get("username"))[0].get("id")
        return redirect("/")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    if request.method == 'POST':

        # check if valid number of stocks
        try:
            shares = request.form.get("shares")
            shares = int(shares)
            if shares <= 0:
                return apology("Please input a positive number of shares")
            if request.form.get("symbol") == None:
                return apology("Please input a valid stock symbol")
        except:
            return apology("Please input a valid number of shares")

        # check if symbol exists
        stock = lookup(request.form.get("symbol"))
        if stock == None:
            return apology("Please input a valid stock symbol")


        # check if user has enough stock
        transactions = db.execute("SELECT shares FROM transactions WHERE id = ? AND symbol = ?", session["user_id"], request.form.get("symbol").upper())
        total = 0
        for transaction in transactions:
            total += transaction["shares"]
        if shares > total:
            return apology("Not enough shares")

        # set cash in database to new amount
        cur_money = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0].get("cash")
        cur_money += stock["price"] * shares
        db.execute("UPDATE users SET cash = ? WHERE id = ?", cur_money, session["user_id"])

        # input new row into transaction table
        db.execute("INSERT INTO transactions (id, name, symbol, price, shares) VALUES (?, ?, ?, ?, ?)", session["user_id"], stock["name"], stock["symbol"], stock["price"], 0 - shares)

        return redirect("/")

    else:
        # calculate which shares and how many the user has to populate select table
        transactions = db.execute("SELECT symbol, shares FROM transactions WHERE id = ?", session["user_id"])

        # sum up all transactions for specific stocks and store in portfolio dictionary
        portfolio = {}
        for transaction in transactions:
            try:
                portfolio[transaction["symbol"]] += transaction["shares"]
            except:
                # case for new stock in transactions, initialise key with number of shares
                portfolio.update({transaction["symbol"] : transaction["shares"]})

        # remove keys that have 0 stocks to prevent user from selecting them
        delkeys = []
        for symbols in portfolio:
            if portfolio[symbols] == 0:
                delkeys.append(symbols)

        for i in delkeys:
            portfolio.pop(i)

        return render_template("sell.html", portfolio=portfolio)
