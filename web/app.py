from flask import Flask, render_template
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    data = {"name": "kan", "age": "18", "salary": "5000"}
    return render_template("index.html", data=data)


@app.route("/abount")
def abount():
    products = ["A", "B", "C"]
    return render_template("abount.html", products_list=products)


@app.route("/admin")
def admin():
    user = "kanjicool"
    return render_template("admin.html", user_name=user)


@app.route("/user/<name>/<age>")
def member(name, age):
    return "<h1>name : {}, age : {}</h1>".format(name, age)


if __name__ == "__main__":
    app.run(debug=True)
