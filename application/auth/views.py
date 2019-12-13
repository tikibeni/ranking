from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user

from application import app, db, login_manager, login_required
from application.auth.models import User
from application.roolit.models import Rooli
from application.auth.forms import LoginForm, RegisterForm, AdminEditForm

# Sisäänkirjautuminen
@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "Käyttäjätunnus ja salasana eivät täsmää")

    login_user(user)
    return redirect(url_for("index"))

# Uloskirjautuminen
@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

# Lomake rekisteröintiä varten
@app.route("/auth/new/", methods=["GET"])
def auth_form():
    return render_template("auth/registerform.html", form = RegisterForm())

# Rekisteröinnin suorittaminen
@app.route("/auth/", methods = ["POST"])
def auth_create():
    form = RegisterForm(request.form)

    if not form.validate():
        return render_template("auth/registerform.html", form = form)

    uusiKayttaja = User(form.name.data, form.username.data, form.password.data, 3)

    db.session().add(uusiKayttaja)
    db.session().commit()

    return redirect(url_for("auth_login"))

# Tunnusten listaaminen adminin hallintasivulle
@app.route("/auth/list/", methods=["GET"])
@login_required(role="admin")
def auth_index():
    return render_template("auth/userctrl.html", tunnukset = User.kayttajatRoolit())

# Toimitetaan lomake ja käyttäjätiedot muokkausta varten
@app.route("/auth/<account_id>/", methods=["GET"])
@login_required(role="admin")
def auth_show(account_id):
    tunnus = User.query.get(account_id)
    return render_template("auth/useredit.html", form = AdminEditForm(obj=tunnus), tunnus=tunnus)

# Toimitetaan muokatut (nimi, rooli) tiedot tietokantaan
@app.route("/auth/<account_id>/", methods=["POST"])
@login_required(role="admin")
def auth_edit(account_id):
    form = AdminEditForm(request.form)
    tunnus = User.query.get(account_id)

    if not form.validate():
        return render_template("auth/useredit.html", tunnus=tunnus, form=form)

    tunnus.name = form.name.data
    tunnus.rooli_id = request.form.get('rooli_id', type=int)
    
    db.session().commit()
    
    return redirect(url_for("auth_index"))

# Tunnuksen poistaminen. Failsafe ettei pysty poistamaan omaa admin-tunnusta.
@app.route("/auth/delete/<account_id>/", methods=["POST"])
@login_required(role="admin")
def auth_delete(account_id):
    if account_id != current_user.id:
        tunnus = User.query.get(account_id)
        db.session().delete(tunnus)
        db.session().commit()
        return redirect(url_for("auth_index"))
    else:
        return redirect(url_for("auth_index"))

# Kilpailija-olion liittäminen tunnukseen
@app.route("/auth/connect/<kilpailija_id>/", methods=["POST"])
@login_required(role="kilpailija")
def auth_connect(kilpailija_id):
    tunnus = User.query.get(current_user.get_id())
    tunnus.kilpailija_id = kilpailija_id

    db.session().commit()

    return redirect(url_for("kilpailijat_index"))

# Toiminnallisuus Kilpailija-User-linkin poistamiseksi (kilpailija-rooli)
@app.route("/auth/disconnect/", methods=["POST"])
@login_required(role="kilpailija")
def auth_disconnect():
    tunnus = User.query.get(current_user.get_id())
    tunnus.kilpailija_id = None

    db.session().commit()

    return redirect(url_for("index"))

# Linkin poistaminen käyttäjänhallintasivun kautta adminin toimesta
@app.route("/auth/disconnect/<account_id>/", methods=["POST"])
@login_required(role="admin")
def auth_disconnect_admin(account_id):
    tunnus = User.query.get(account_id)
    tunnus.kilpailija_id = None

    db.session().commit()

    return redirect(url_for('auth_index'))