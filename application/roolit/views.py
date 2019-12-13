from flask import render_template, request, redirect, url_for
from flask_login import current_user

from application import app, db, login_manager, login_required
from application.roolit.models import Rooli
from application.roolit.forms import RooliForm

# Roolien toimittaminen list.html
@app.route("/roolit/", methods=["GET"])
@login_required(role="admin")
def roolit_index():
	return render_template("roolit/list.html", roolit = Rooli.query.all())

# Lomakkeen hakeminen roolin luomista varten
@app.route("/roolit/new/", methods=["GET"])
@login_required(role="admin")
def roolit_form():
	return render_template("roolit/new.html", form = RooliForm())

# Roolin hakeminen muokkausta varten
@app.route("/roolit/<rooli_id>/", methods=["GET"])
@login_required(role="admin")
def roolit_show(rooli_id):
	rooli = Rooli.query.get(rooli_id)
	return render_template("roolit/edit.html", rooli = rooli, form = RooliForm(obj=rooli))

# Luomislomakkeen tietojen käsittely ja Roolin luominen
@app.route("/roolit/", methods=["POST"])
@login_required(role="admin")
def roolit_create():
	form = RooliForm(request.form)

	if not form.validate():
		return render_template("roolit/new.html", form = form)

	r = Rooli(form.name.data)

	db.session().add(r)
	db.session().commit()

	return redirect(url_for("roolit_index"))

# Muokkauslomakkeen tietojen käsittely ja Roolin muokkaus
@app.route("/roolit/<rooli_id>/", methods=["POST"])
@login_required(role="admin")
def roolit_edit(rooli_id):
	form = RooliForm(request.form)
	rooli = Rooli.query.get(rooli_id)

	if not form.validate():
		return render_template("roolit/edit.html", rooli = rooli, form = form)
	
	rooli.name = form.name.data
	db.session().commit()

	return redirect(url_for("roolit_index"))

# Roolin poistaminen
@app.route("/roolit/delete/<rooli_id>", methods=["POST"])
@login_required(role="admin")
def roolit_delete(rooli_id):
	rooli = Rooli.query.get(rooli_id)
	db.session().delete(rooli)
	db.session().commit()

	return redirect(url_for("roolit_index"))