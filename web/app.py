from flask import Flask, render_template
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello flask Framework</h1>"


@app.route("/abount")
def abount():
    return "<h1>abount us </h1>"


@app.route("/admin")
def admin():
    return "<h1>!ADMIN! </h1>"


@app.route("/user/<name>/<age>")
def member(name, age):
    return "<h1>name : {}, age : {}</h1>".format(name, age)


if __name__ == "__main__":
    app.run(debug=True)
