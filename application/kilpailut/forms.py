from flask_wtf import FlaskForm
from application import db
from wtforms import StringField, DateField, SelectField, validators
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from application.luokat.models import Luokka

# Päivämäärien validointi!
# Luokka_id:n määrittely

class KilpailuForm(FlaskForm):
	name = StringField("Nimi:", [validators.Length(min=2, max=20)])
	venue = StringField("Kilpailupaikka: ", [validators.Length(min=3, max=30)])
	startdate = DateField("Alkamispäivä: ")
	enddate = DateField("Loppumispäivä: ")
	luokka_id = QuerySelectField('Luokka: ', query_factory=lambda: Luokka.query.all())

	class Meta:
		csrf = False