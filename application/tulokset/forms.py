from flask_wtf import FlaskForm

from sqlalchemy import text

from wtforms import Form, StringField, IntegerField, validators
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from application import db
from application.kilpailut.models import Kilpailu
from application.kilpailijat.models import Kilpailija

# Lomake tuloksia varten
class TulosForm(FlaskForm):
    sijoitus = IntegerField("Sijoitus: ")
    pisteet = IntegerField("Pistemäärä: ")
    kilpailu_id = StringField("Kilpailu: ")
    kilpailija_id = QuerySelectField("Kilpailija: ", query_factory=lambda: Kilpailija.query.all(), get_label='name')

    # Validaattori, joka tarkistaa tulosten loogisuuden.
    def validate(self):
        # Attribuutteihin (Models.py) rakennetut validoinnit:
        if not Form.validate(self):
            return False
        else:
            return True

    class Meta:
        csrf = False