from flask_wtf import FlaskForm
from wtforms import StringField, validators

from application import db
from application.kilpailut.models import Kilpailu

# Lomake taulua 'Kilpailija' varten
class KilpailijaForm(FlaskForm):
    name = StringField("Nimi: ", [validators.Length(min=5, max=50)])
    sailnumber = StringField("Purjenumero: ", [validators.Length(min=4, max=10, message="Syötä muodossa: esim. FIN-X")])
    sailclub = StringField("Pursiseura: ", [validators.Length(min=2, max=25)])

    class Meta:
        csrf = False