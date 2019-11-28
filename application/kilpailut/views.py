from flask import render_template, request, redirect, url_for
from flask_login import login_required

from application import app, db
from application.kilpailut.models import Kilpailu
from application.kilpailut.forms import KilpailuForm
from application.luokat.models import Luokka

@app.route("/kilpailut", methods=["GET"])
def kilpailut_index():
    return render_template("kilpailut/list.html", kilpailut = Kilpailu.query.all())

# Tähän liitetty luokkien tulostus sivulle:

@app.route("/kilpailut/new/", methods=["GET"])
@login_required
def kilpailut_form():
    return render_template("kilpailut/new.html", form = KilpailuForm())

# Luokka_id:n selvittäminen!

@app.route("/kilpailut/", methods=["POST"])
@login_required
def kilpailut_create():
    form = KilpailuForm(request.form)

    if not form.validate():
        return render_template("kilpailut/new.html", form = form)

    k = Kilpailu(form.name.data, form.venue.data, form.startdate.data, form.enddate.data, form.luokka_id.data)

    db.session().add(k)
    db.session().commit()

    return redirect(url_for("kilpailut_index"))
