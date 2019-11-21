from flask import render_template, request, redirect, url_for
from flask_login import login_required

from application import app, db
from application.luokat.models import Luokka
from application.luokat.forms import LuokkaForm

@app.route("/")
def home():
	return render_template("/")

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

@app.route("/luokat/delete/<luokka_id>", methods=["POST"])
# @login_required
def luokat_delete(luokka_id):
	
	luokka = Luokka.query.get(luokka_id)
	db.session.delete(luokka)
	db.session().commit()

	return redirect(url_for("luokat_index"))

@app.route("/luokat/edit/<luokka_id>", methods=["POST"])
# @login_required
def luokat_edit(luokka_id):
	
	luokka = Luokka.query.get(luokka_id)

	form = LuokkaForm(request.form)
	if request.method == "POST" and form.validate():
		save_changes(luokka, form)
		return redirect(url_for("luokat_index"))
	
	return render_template("luokat/edit.html", form=form, luokka=luokka)

def save_changes(luokka, form, new=False):
	luokka.name = form.name.data
	db.session().commit()