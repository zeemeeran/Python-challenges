
import re
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    title = "About page!!!!!!!"
    names = ["Adam", "John", "Jake"]
    return render_template("about.html", title=title, names=names)


@app.route("/admin")
def admin():
    return redirect(url_for("index"))

#if __name__ == '__main__' :
 #   app.run(debug=True)

app.run()

