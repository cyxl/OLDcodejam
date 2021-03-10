from flask import render_template, Blueprint
from src import config

view = Blueprint("views", __name__)


@view.route("/")
@view.route("/home")
def home():
    return render_template("index.html")


@view.route("/cj")
def code_jam():
    return
    # TODO make function's for yt twitch etc.
    # TODO make html files for the buttons and more.
    # TODO find out how to read a text box with python that is made in html.
