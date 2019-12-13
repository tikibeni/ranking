from application import db
from sqlalchemy import text

# Käyttäjätaulu
class User(db.Model):
	__tablename__ = "account"

	id = db.Column(db.Integer, primary_key=True)
	date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
	date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
				  onupdate=db.func.current_timestamp())
	name = db.Column(db.String(144), nullable=False)
	username = db.Column(db.String(144), nullable=False)
	password = db.Column(db.String(144), nullable=False)
	rooli_id = db.Column(db.Integer, db.ForeignKey('rooli.id'),
		nullable=True)
	kilpailija_id = db.Column(db.Integer, db.ForeignKey('kilpailija.id'))

	def __init__(self, name, username, password, rooli_id):
		self.name = name
		self.username = username
		self.password = password
		self.rooli_id = rooli_id

	def get_id(self):
		return self.id

	def get_role(self):
		return self.rooli_id

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def is_authenticated(self):
		return True

	# Metodi käyttäjienhallintasivua varten
	@staticmethod
	def kayttajatRoolit():
		stmt = text("SELECT account.id, account.username, account.name, Rooli.name, Kilpailija.name, account.date_created, account.date_modified"
					" FROM account"
					" LEFT JOIN Rooli ON Rooli.id = account.rooli_id"
					" LEFT JOIN Kilpailija ON Kilpailija.id = account.kilpailija_id")
		res = db.engine.execute(stmt)

		response = []
		for row in res:
			response.append({"kaytid":row[0],"kayttunnus":row[1],"kaytnimi":row[2],"kaytrooli":row[3],"kilpailija":row[4],"kaytluot":row[5],"kaytmuok":row[6]})

		return response
	
	# Metodi kilpailijat list.html varten, jottei samaa kilpailijaa voida liittää useampaan käyttäjään
	@staticmethod
	def kilpailijaLinkki():
		stmt = text("SELECT account.kilpailija_id FROM account"
					" LEFT JOIN Kilpailija ON Kilpailija.id = account.kilpailija_id"
					" WHERE account.kilpailija_id")
		res = db.engine.execute(stmt)

		response = []
		for row in res:
			response.append({"kaytkilpid":row[0]})

		return response