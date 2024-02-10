from flask import (
    Blueprint,
    render_template,
    session,
    url_for,
    redirect,
    make_response,
    request,
    flash,
)
from web import db

cart = Blueprint("cart", __name__)


# @cart.route("/cart", methods=["GET", "POST"])
# def cart_page():
#     return render_template("cart.html")
