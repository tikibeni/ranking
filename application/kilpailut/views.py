from flask import render_template, request, redirect, url_for

from flask_login import login_required

from application import app, db
from application.luokat.models import Luokka
from application.kilpailut.models import Kilpailu
from application.kilpailut.forms import KilpailuForm

@app.route("/kilpailut", methods=["GET"])
def kilpailut_index():
    return render_template("kilpailut/list.html", kilpailut = Kilpailu.query.all())

@app.route("/kilpailut/new/", methods=["GET"])
@login_required
def kilpailut_form():
    return render_template("kilpailut/new.html", form = KilpailuForm())

@app.route("/kilpailut/<kilpailu_id>/", methods=["GET"])
@login_required
def kilpailut_show(kilpailu_id):
	kilpailu = Kilpailu.query.get(kilpailu_id)
	return render_template("kilpailut/edit.html", kilpailu = kilpailu, form = KilpailuForm(obj=kilpailu))

@app.route("/kilpailut/", methods=["POST"])
@login_required
def kilpailut_create():
    form = KilpailuForm(request.form)

    if not form.validate():
        return render_template("kilpailut/new.html", form = form)

    luokkaId = request.form.get('luokka_id', type=int)
    kilpailu = Kilpailu(form.name.data, form.venue.data, form.startdate.data, form.enddate.data, luokkaId)

    db.session().add(kilpailu)
    db.session().commit()

    return redirect(url_for("kilpailut_index"))

@app.route("/kilpailut/<kilpailu_id>/", methods=["POST"])
@login_required
def kilpailut_edit(kilpailu_id):
    form = KilpailuForm(request.form)
    kilpailu = Kilpailu.query.get(kilpailu_id)

    if not form.validate():
        return render_template("kilpailut/edit.html", form = form)

    kilpailu.name = form.name.data
    kilpailu.venue = form.venue.data
    kilpailu.startdate = form.startdate.data
    kilpailu.enddate = form.enddate.data
    kilpailu.luokka_id = request.form.get('luokka_id', type=int)

    db.session().commit()

    return redirect(url_for("kilpailut_index"))

@app.route("/kilpailut/delete/<kilpailu_id>", methods=["POST"])
@login_required
def kilpailut_delete(kilpailu_id):
	kilpailu = Kilpailu.query.get(kilpailu_id)
	db.session.delete(kilpailu)
	db.session().commit()

	return redirect(url_for("kilpailut_index"))