import os

from paths import TEMPLATES_PATH

from dotenv import load_dotenv
from flask import Flask, request, session, render_template

load_dotenv('.env')

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY")

MENU_ITEMS = [
        {'url': 'feed', 'label': 'Feed'},
        {'url': 'search', 'label': 'Find users'},
        {'url': 'logout', 'label': 'Logout'}
    ]


@app.route("/")
def home():
    return render_template('base.html', menu_items=MENU_ITEMS, title='Base')


@app.route("/sign_up")
def sign_up():
    return render_template('sign_up.html', title='Signing up')


@app.route("/confirm_code")
def confirm_code():
    return render_template('confirmcode.html', title='Confirmation')


@app.route('/login')
def login():
    return render_template('login.html', title='Login')


@app.route("/feed")
def feed():
    return render_template('feed.html', menu_items=MENU_ITEMS, title='Feed')


@app.route("/profile")
def profile():
    return render_template('profile.html', menu_items=MENU_ITEMS, title='Profile')


@app.route("/search")
def search():
    return render_template('search.html', menu_items=MENU_ITEMS, title='Search')


@app.route("/myprofile")
def myprofile():
    return render_template('myprofile.html', menu_items=MENU_ITEMS, title='My profile')


@app.route("/edit_post")
def edit_post():
    return render_template('edit_post.html', menu_items=MENU_ITEMS, title='Editing')


if __name__ == "__main__":
    app.run(debug=True)
