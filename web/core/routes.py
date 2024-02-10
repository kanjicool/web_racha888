from flask import Blueprint, render_template, request, redirect, flash, url_for
from web.shop.models import Product, Category
from web import db

core = Blueprint("core", __name__, static_folder="static")


@core.route("/")
def home():

    return render_template("home.html")


@core.route("/about")
def about():
    return render_template("about.html")
