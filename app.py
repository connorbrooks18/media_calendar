from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# @app.route("/view/<name>/")
# def media(name):
#     return "Cannot get '" + name + "'"

#This is a change made by Mark Earl Brooks on Saturday
 


if __name__ == '__main__':
    app.run(debug=True)