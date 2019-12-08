from application import db

# Kilpailija-taulun määrittäminen
class Kilpailija(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    sailnumber = db.Column(db.String(10), nullable=False)
    sailclub = db.Column(db.String(25), nullable=False)

    kilpailut = db.relationship('Kilpailu', secondary = 'liitostaulu')

    def __init__(self,name,sailnumber,sailclub):
        self.name=name
        self.sailnumber=sailnumber
        self.sailclub=sailclub