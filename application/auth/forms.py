from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, IntegerField, validators

from application import db
from application.auth.models import User
from application.roolit.models import Rooli

from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField

# Lomake kirjautumista varten
class LoginForm(FlaskForm):
	username = StringField("Käyttäjätunnus")
	password = PasswordField("Salasana")

	class Meta:
		csrf = False

# Lomake rekisteröintiä varten
class RegisterForm(FlaskForm):
	name = StringField("Nimi: ", [validators.Length(min=2, max=30)])
	username = StringField("Käyttäjätunnus: ", [validators.Length(min=2, max=20)])
	password = PasswordField("Salasana: ", [
		validators.Required(),
		validators.EqualTo('varmistaja', message="Salasanojen täytyy täsmätä")
	])
	varmistaja = PasswordField("Salasana uudelleen: ")

	class Meta:
		csrf = False

# Lomake editointia varten
class AdminEditForm(FlaskForm):
	id = IntegerField("ID: ", [validators.DataRequired()])
	username = StringField("Käyttäjätunnus: ", [validators.Length(min=2, max=20)])
	name = StringField("Nimi: ", [validators.Length(min=2, max=30)])
	rooli_id = QuerySelectField("Käyttäjäryhmä: ", query_factory=lambda: Rooli.query.all(), get_label='name')

	class Meta:
		csrf = False