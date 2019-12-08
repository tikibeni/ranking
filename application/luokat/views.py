from flask import render_template, request, redirect, url_for
from flask_login import current_user

from application import app, db, login_manager, login_required
from application.luokat.models import Luokka
from application.luokat.forms import LuokkaForm

# Luokkien toimittaminen list.html
@app.route("/luokat/", methods=["GET"])
def luokat_index():
	return render_template("luokat/list.html", luokat = Luokka.query.all())

# Lomakkeen hakeminen luokan luomista varten
@app.route("/luokat/new/", methods=["GET"])
@login_required(role="admin")
def luokat_form():
	return render_template("luokat/new.html", form = LuokkaForm())

# Luokan hakeminen muokkausta varten
@app.route("/luokat/<luokka_id>/", methods=["GET"])
@login_required(role="admin")
def luokat_show(luokka_id):
	luokka = Luokka.query.get(luokka_id)
	return render_template("luokat/edit.html", luokka = luokka, form = LuokkaForm(obj=luokka))

# Luomislomakkeen tietojen käsittely ja Luokan luominen
@app.route("/luokat/", methods=["POST"])
@login_required(role="admin")
def luokat_create():
	form = LuokkaForm(request.form)

	if not form.validate():
		return render_template("luokat/new.html", form = form)

	l = Luokka(form.name.data)

	db.session().add(l)
	db.session().commit()

	return redirect(url_for("luokat_index"))

# Muokkauslomakkeen tietojen käsittely ja Luokan muokkaus
@app.route("/luokat/<luokka_id>/", methods=["POST"])
@login_required(role="admin")
def luokat_edit(luokka_id):
	form = LuokkaForm(request.form)
	luokka = Luokka.query.get(luokka_id)

	if not form.validate():
		return render_template("luokat/edit.html", luokka = luokka, form = form)
	
	luokka.name = form.name.data
	db.session().commit()

	return redirect(url_for("luokat_index"))

# Luokan poistaminen
@app.route("/luokat/delete/<luokka_id>", methods=["POST"])
@login_required(role="admin")
def luokat_delete(luokka_id):
	luokka = Luokka.query.get(luokka_id)
	db.session().delete(luokka)
	db.session().commit()

	return redirect(url_for("luokat_index"))