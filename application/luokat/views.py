from flask import render_template, request, redirect, url_for
from flask_login import login_required

from application import app, db
from application.luokat.models import Luokka
from application.luokat.forms import LuokkaForm

@app.route("/luokat", methods=["GET"])
def luokat_index():
	return render_template("luokat/list.html", luokat = Luokka.query.all())

@app.route("/luokat/new/")
@login_required
def luokat_form():
	return render_template("luokat/new.html", form = LuokkaForm())

@app.route("/luokat/", methods=["POST"])
@login_required
def luokat_create():
	form = LuokkaForm(request.form)

	if not form.validate():
		return render_template("luokat/new.html", form = form)

	l = Luokka(form.name.data)

	db.session().add(l)
	db.session().commit()

	return redirect(url_for("luokat_index"))