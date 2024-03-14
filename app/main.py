import os

from dotenv import load_dotenv

from flask import Flask, request

load_dotenv('.env')

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY")


@app.route("/")
def home():
    return "home page"


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return "post method on login page"
    else:
        return "get method on login page"


if __name__ == "__main__":
    app.run(debug=True)
