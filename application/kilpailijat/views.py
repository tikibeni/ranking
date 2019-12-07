from flask import render_template, request, redirect, url_for

from flask_login import login_required

from application import app, db
from application.kilpailijat.models import Kilpailija
from application.kilpailijat.forms import KilpailijaForm

# Haetaan kaikki kilpailijat list.html:ään
@app.route("/kilpailijat/", methods=["GET"])
def kilpailijat_index():
    return render_template("kilpailijat/list.html", kilpailijat=Kilpailija.query.all())

# Haetaan lomake uuden kilpailijan luomista varten new.html:ään
@app.route("/kilpailijat/new/", methods=["GET"])
@login_required
def kilpailijat_form():
    return render_template("kilpailijat/new.html", form=KilpailijaForm())

# Haetaan muokattava kilpailija id:n avulla muokkaamista varten edit.html:ään
@app.route("/kilpailijat/<kilpailija_id>/", methods=["GET"])
@login_required
def kilpailijat_show(kilpailija_id):
    kilpailija = Kilpailija.query.get(kilpailija_id)
    return render_template("kilpailijat/edit.html", kilpailija=kilpailija, form=KilpailijaForm(obj=kilpailija))

# Haetaan syötetyt tiedot lomakkeesta Kilpailija-olion luomista varten
@app.route("/kilpailijat/", methods=["POST"])
@login_required
def kilpailijat_create():
    form = KilpailijaForm(request.form)

    if not form.validate():
        return render_template("kilpailijat/new.html", form=form)

    kil = Kilpailija(form.name.data, form.sailnumber.data, form.sailclub.data)

    db.session().add(kil)
    db.session().commit()

    return redirect(url_for("kilpailijat_index"))

# Käsitellään lomakkeeseen laitetut tiedot ja muokataan kilpailijan tietoja
@app.route("/kilpailijat/<kilpailija_id>/", methods=["POST"])
@login_required
def kilpailijat_edit(kilpailija_id):
    form = KilpailijaForm(request.form)
    kilpailija = Kilpailija.query.get(kilpailija_id)

    if not form.validate():
        return render_template("kilpailijat/edit.html", kilpailija=kilpailija, form=form)

    kilpailija.name = form.name.data
    kilpailija.sailnumber = form.sailnumber.data
    kilpailija.sailclub = form.sailclub.data

    db.session().commit()

    return redirect(url_for("kilpailijat_index"))

# Poistetaan kilpailja sen id:n perusteella
@app.route("/kilpailjat/delete/<kilpailija_id>", methods=["POST"])
@login_required
def kilpailijat_delete(kilpailija_id):
    kilpailija = Kilpailija.query.get(kilpailija_id)
    db.session().delete(kilpailija)
    db.session().commit()

    return redirect(url_for("kilpailut_index"))