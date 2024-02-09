from flask import Flask, session

app = Flask(__name__, static_folder="images/")


# Flask blueprints
from web.core.routes import core
from web.shop.routes import shop
from web.cart.routes import cart


app.register_blueprint(core)
app.register_blueprint(shop)
app.register_blueprint(cart)
