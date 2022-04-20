from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to customer database!"

@app.route("/about")
def about():
    return "This is the about page"

if __name__ == '__main__' :
    app.run(debug=True)



