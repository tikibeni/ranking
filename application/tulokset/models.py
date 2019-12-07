from application import db

class Tulos(db.Model):
    __tablename__='liitostaulu'
    id = db.Column(db.Integer, primary_key=True)
    sijoitus = db.Column(db.Integer, nullable=True)
    
    kilpailu_id = db.Column(db.Integer, db.ForeignKey('kilpailu.id'), nullable=False)
    kilpailija_id = db.Column(db.Integer, db.ForeignKey('kilpailija.id'), nullable=False)