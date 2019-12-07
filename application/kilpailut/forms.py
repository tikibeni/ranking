from flask_wtf import FlaskForm

from application import db
from application.luokat.models import Luokka

from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms import Form, StringField, DateTimeField, validators

class KilpailuForm(FlaskForm):
	name = StringField("Nimi:", [validators.Length(min=2, max=20)])
	venue = StringField("Kilpailupaikka: ", [validators.Length(min=3, max=30)])
	startdate = DateTimeField("Alkamispäivä: ", [validators.DataRequired(message="Syötä alkupäivämäärä muodossa: yyyy-mm-dd hh:mm:ss!")])
	enddate = DateTimeField("Loppumispäivä: ", [validators.DataRequired(message="Syötä loppupäivämäärä muodossa: yyyy-mm-dd hh:mm:ss!")])
	luokka_id = QuerySelectField("Luokka: ", query_factory=lambda: Luokka.query.all(), get_label='name')

	def validate(self):
		if not Form.validate(self):
			return False
		if self.enddate.data < self.startdate.data:
			return False
		else:
			return True

	class Meta:
		csrf = False