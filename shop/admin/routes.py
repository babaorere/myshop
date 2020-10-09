from flask import render_template
from shop import app

@app.route("/")
def home():
    return "Home page"


@app.route("/register/")
def register():
    return render_template("admin/register.html", title="Register user")