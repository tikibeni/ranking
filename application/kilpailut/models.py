from application import db
from datetime import datetime

# Lisää väliin vielä db.relationship tauluun Tulos, kun tämän taulun CRUD on toimiva.

class Kilpailu(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50), nullable=False)
	venue = db.Column(db.String(30))
	startdate = db.Column(db.DateTime)
	enddate = db.Column(db.DateTime)
	luokka_id = db.Column(db.Integer, db.ForeignKey('luokka.id'),
		nullable=False)

	def __init__(self,name,venue,startdate,enddate,luokka_id):
		self.name = name
		self.venue = venue
		self.startdate = startdate
		self.enddate = enddate
		self.luokka_id = luokka_id