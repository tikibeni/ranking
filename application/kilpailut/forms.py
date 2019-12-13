from flask_wtf import FlaskForm

from application import db
from application.luokat.models import Luokka

from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.fields.html5 import DateField
from wtforms import Form, StringField, validators, ValidationError

# Lomake Kilpailua varten
class KilpailuForm(FlaskForm):
	name = StringField("Nimi:", [validators.Length(min=2, max=40)])
	venue = StringField("Kilpailupaikka: ", [validators.Length(min=3, max=30)])
	startdate = DateField("Alkamispäivä: ", [validators.DataRequired(message="Syötä alkupäivämäärä muodossa: dd-mm-yyyy!")])
	enddate = DateField("Loppumispäivä: ", [validators.DataRequired(message="Syötä loppupäivämäärä muodossa: dd-mm-yyyy!")])
	luokka_id = QuerySelectField("Luokka: ",[validators.DataRequired(message="Valitse luokka")], query_factory=lambda: Luokka.query.all(), get_label='name', allow_blank=True, blank_text="Valitse luokka")

	# Validaattori, joka tarkistaa kilpailun päivämäärien loogisuuden
	def validate(self):
		if not Form.validate(self):
			return False
		if self.enddate.data < self.startdate.data:
			return False
		else:
			return True

	class Meta:
		csrf = False