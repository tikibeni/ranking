from flask_wtf import FlaskForm
from wtforms import StringField, validators

class LuokkaForm(FlaskForm):
	name = StringField("Luokan nimi:", [validators.Length(min=2, max=20)])

	class Meta:
		csrf = False
