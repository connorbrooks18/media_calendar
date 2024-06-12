from flask import Flask, render_template

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
# def media(name):
#     return "Cannot get '" + name + "'"


 


if __name__ == '__main__':
    app.run(debug=True)