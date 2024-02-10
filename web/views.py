from flask import Blueprint, render_template, request

views = Blueprint("views", __name__)


@views.route("/")
def home():
    return render_template('home.html')

@views.route("/about")
def about():
    return render_template('about.html')

@views.route("/contact")
def contact():
    return render_template('contact.html')

@views.route("/s1")
def s1():
    return render_template('s1.html')

@views.route("/s2")
def s2():
    return render_template('s2.html')

@views.route("/s3")
def s3():
    return render_template('s3.html')

@views.route("/s4")
def s4():
    return render_template('s4.html')

@views.route("/s5")
def s5():
    return render_template('s5.html')
