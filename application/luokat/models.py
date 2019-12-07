from application import db
from sqlalchemy.sql import text

class Luokka(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20), nullable=False)
	kilpailut = db.relationship("Kilpailu", backref='luokka', lazy=True)

	def __init__(self,name):
		self.name = name

	def get_id(self):
		return self.id

	def get_name(self):
		return self.name