from flask import Flask, render_template, request, url_for
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/admin")
def admin():
    user = "kanjicool"
    return render_template("admin.html", user_name=user)


@app.route("/user/<name>")
def member(name):
    return "<h1>name : {}</h1>".format(name)


@app.route("/test")
def test():
    return render_template("test.html")


@app.route("/top_up")
def top_up():
    return render_template("top_up.html")


@app.route("/sen_data")
def signupForm():
    name = request.args.get("name")
    description = request.args.get("description")
    return render_template(
        "thankyou.html", data={"name": name, "desciption": description}
    )


if __name__ == "__main__":
    app.run(debug=True)
