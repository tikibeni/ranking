from application import app, db
from flask import redirect, render_template, request, url_for
from application.luokat.models import Luokka

@app.route("/luokat", methods=["GET"])
def luokat_index():
	return render_template("luokat/list.html", luokat = Luokka.query.all())

@app.route("/luokat/new/")
def luokat_form():
	return render_template("luokat/new.html")

@app.route("/luokat/", methods=["POST"])
def luokat_create():
	l = Luokka(request.form.get("name"))

	db.session().add(l)
	db.session().commit()

	return redirect(url_for("luokat_index"))
