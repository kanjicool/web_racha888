from flask import Blueprint, render_template, request, session
from web.shop.models import Product, Category

from web import db

shop = Blueprint("shop", __name__)


@shop.route("/details", methods=["POST", "GET"])
def details():
    return render_template("details.html")


@shop.route("/search")
def search():
    return render_template("search.html")


@shop.route("/main-shop")
def main_shop():

    return render_template("shop.html")
