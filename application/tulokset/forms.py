from flask_wtf import FlaskForm
from wtforms import IntegerField, validators

class TulosForm(FlaskForm):
    sijoitus = IntegerField("Sijoitus: ", [validators.Length(min=1, max=100)])

    class Meta:
        csrf = False