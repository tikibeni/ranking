from flask_wtf import FlaskForm
from wtforms import StringField, validators

# Lomake roolia varten
class RooliForm(FlaskForm):
	name = StringField("Nimi:", [validators.Length(min=2, max=20)])

	class Meta:
		csrf = False