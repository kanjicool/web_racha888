from flask import Blueprint, render_template, request, redirect, flash, url_for


core = Blueprint("core", __name__, static_folder="static")


@core.route("/")
def home():
    return render_template("home.html")
