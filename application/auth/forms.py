from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

class LoginForm(FlaskForm):
	username = StringField("Käyttäjätunnus")
	password = PasswordField("Salasana")

	class Meta:
		csrf = False

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