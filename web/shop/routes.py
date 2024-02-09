from flask import Blueprint, render_template, request, session

shop = Blueprint("shop", __name__)


@shop.route("/details", methods=["POST", "GET"])
def details():
    return render_template("details.html")


@shop.route("/search")
def search():
    return render_template("search.html")
