from flask import render_template, request, redirect, url_for
from flask_login import current_user

from application import app, db, login_manager, login_required
from application.tulokset.models import Tulos
from application.kilpailut.models import Kilpailu
from application.kilpailijat.models import Kilpailija
from application.tulokset.forms import TulosForm

# Toimitetaan halutun kilpailun infot luomislomaketta varten
@app.route("/tulokset/new/<kilpailu_id>/", methods=["GET"])
@login_required(role="admin")
def tulokset_form(kilpailu_id):
    kilpailu = Kilpailu.query.get(kilpailu_id)
    return render_template("tulokset/new.html", form = TulosForm(obj=kilpailu_id), kilpailu=kilpailu)

# Haetaan kilpailun tulokset kilpailun id:n perusteella ja toimitetaan taulukko.html 
@app.route("/tulokset/<kilpailu_id>/", methods=["GET"])
def tulokset_show(kilpailu_id):
    return render_template("tulokset/taulukko.html", kilpailun_Tulokset=Tulos.kilpailunTulokset(kilpailu_id) )

# Noudetaan luomistiedot lomakkeesta ja luodaan uusi Tulos-olio
@app.route("/tulokset/new/<kilpailu_id>/", methods=["POST"])
@login_required(role="admin")
def tulokset_create(kilpailu_id):
    form = TulosForm(request.form)
    kilpailu = Kilpailu.query.get(kilpailu_id)

    if not form.validate():
        return render_template("tulokset/new.html", form=form, kilpailu=kilpailu)

    kilpailuID = kilpailu_id
    kilpailijaID = request.form.get('kilpailija_id', type=int)
    tulos = Tulos(form.sijoitus.data, form.pisteet.data, kilpailuID, kilpailijaID)

    db.session().add(tulos)
    db.session().commit()

    return redirect(url_for("kilpailut_index"))

'''
@app.route("/tulokset/<tulos_id>/", methods=["POST"])
@login_required(role="admin")
def tulokset_edit(tulos_id):
    form = TulosForm(request.form)
    tulos = Tulos.query.get(tulos_id)

    if not form.validate():
        return render_template("tulokset/edit.html", form=form, tulos=tulos)

    tulos.sijoitus = form.sijoitus.data
    tulos.kilpailu_id = request.form.get('kilpailu_id', type=int)
    tulos.kilpailija_id = request.form.get('kilpailija_id', type=int)

    db.session().commit()

    return redirect(url_for("kilpailut_index"))

@app.route("/tulokset/delete/<tulos_id>/", methods=["POST"])
@login_required(role="admin")
def tulokset_delete(tulos_id):
    tulos = Tulos.query.get(tulos_id)
    db.session().delete(tulos)
    db.session().commit()

    return redirect(url_for("kilpailut_index"))
'''