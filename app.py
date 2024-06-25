from flask import Flask, render_template, request
from cryptography.fernet import Fernet

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
        for pair in request.form.items():
            print(pair)


        return home()
    else:
        return render_template("login.html" )



def encrypt(password):
    return Fernet("ok").encrypt(password)

 


if __name__ == '__main__':
    app.run(debug=True)