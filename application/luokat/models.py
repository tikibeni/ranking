from application import db

class Luokka(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20), nullable=False)

	def __init__(self,name):
		self.name = name
