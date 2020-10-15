from flask import render_template, request, redirect, url_for, flash

from shop import app, db
from .models import Brand, Category

@app.route("/addbrand", methods=['GET', 'POST'])
def addbrand():
    if request.method == "POST":
        getbrand = request.form.get("brand")
        brand = Brand(name=getbrand)
        db.session.add(brand)
        db.session.commit()
        flash(f'The Brand {getbrand} was added to your database', 'success')
        return redirect(url_for('addbrand'))
    return render_template("products/addbrand.html", brands="brands", title="Add Brand Page")

@app.route("/addcat", methods=['GET', 'POST'])
def addcat():
    if request.method == "POST":
        getcat = request.form.get("category")
        cat = Category(name=getcat)
        db.session.add(cat)
        db.session.commit()
        flash(f'The Category {getcat} was added to your database', 'success')
        return redirect(url_for('addbrand'))
    return render_template("products/addbrand.html", brands="brands", title="Add Brand Page")
