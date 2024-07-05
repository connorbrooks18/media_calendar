from flask import Flask, render_template, request, redirect, url_for
from cryptography.fernet import Fernet
import sqlite3 as sql



with open("key", "r") as f:
    key = f.read()[2:-1]




app = Flask(__name__)

events = [
    ["hehe", "ok", "mike"],
    ["haha"],
    ["woah", "watch"], 
    ["JJK #1", "ONE PIECE"],
    [],
    ["No way", "home"],
    ["NANANa", "Batman"]
]

@app.route("/")
def home():
    return render_template("index.html", week_cal=events)


# @app.route("/view/<name>/")

@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        # for pair in request.form.items():
            #encrypt(bytes(pair[1], "utf8"))


        return redirect(url_for("home"))
    else:
        return render_template("login.html" )

@app.route("/signup", methods = ["POST", "GET"])
def signup():
    if request.method == "POST":
        # for key, value in request.form.items():
        #     print(pair)
        conn = sql.connect("media.db")
        curs = conn.cursor()
        curs.execute("INSERT INTO users VALUES (?, ?, ?, ?)", [value for key, value in request.form.items()])
        print(curs.execute("SELECT * FROM users").fetchall())
        conn.commit()
        curs.close()
        conn.close()

        return redirect(url_for("home"))
    else:
        return render_template("signup.html" )


def encrypt(password):
    return Fernet(key).encrypt(password)

 


if __name__ == '__main__':
    app.run(debug=True)


