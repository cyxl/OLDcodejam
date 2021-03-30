from flask import render_template, Blueprint
from bokeh.embed import components
from bokeh.plotting import figure

view = Blueprint("views", __name__)


@view.route("/")
@view.route("/home")
def home():
    return render_template("index.html")


@view.route("/cj")
@view.route("/stracker")
def stracker():
    return render_template("cj.html")


@view.route("/cj/youtube")
@view.route("stracker/youtube")
def youtube():
    return render_template("youtube.html")


