from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from application import db
from application.kilpailut.models import Kilpailu
from application.kilpailijat.models import Kilpailija

class TulosForm(FlaskForm):
    sijoitus = IntegerField("Sijoitus: ")
    pisteet = IntegerField("Pistemäärä: ")
    kilpailu_id = StringField("Kilpailu: ")
    kilpailija_id = QuerySelectField("Kilpailija: ", query_factory=lambda: Kilpailija.query.all(), get_label='name')

    class Meta:
        csrf = False