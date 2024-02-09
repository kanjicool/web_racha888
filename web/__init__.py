import os
from flask import Flask, session

app = Flask(__name__, static_folder="images/")


# Flask database
from flask_sqlalchemy import SQLAlchemy

app.config["SECRET_KEY"] = "kanjicool"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    os.getcwd(), "sqlite.db"
)
db = SQLAlchemy(app)

# Flask blueprints
from web.core.routes import core
from web.shop.routes import shop
from web.cart.routes import cart


app.register_blueprint(core)
app.register_blueprint(shop)
app.register_blueprint(cart)
