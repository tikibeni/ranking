from application import db
from datetime import datetime
from sqlalchemy import text

# Kilpailu-taulun luominen
class Kilpailu(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50), nullable=False)
	venue = db.Column(db.String(30), nullable=False)
	startdate = db.Column(db.Date, nullable=False)
	enddate = db.Column(db.Date, nullable=False)
	luokka_id = db.Column(db.Integer, db.ForeignKey('luokka.id'),
		nullable=False)

	kilpailijat = db.relationship('Kilpailija', secondary='liitostaulu')

	def __init__(self,name,venue,startdate,enddate,luokka_id):
		self.name = name
		self.venue = venue
		self.startdate = startdate
		self.enddate = enddate
		self.luokka_id = luokka_id

	# Metodi tulevien kilpailujen hakua varten -> Etusivulle
	@staticmethod
	def tulevatKilpailut():
		stmt = text("SELECT Luokka.name, Kilpailu.name, Kilpailu.startdate, Kilpailu.enddate FROM Kilpailu"
					" LEFT JOIN Luokka ON Luokka.id = Kilpailu.luokka_id"
					" WHERE Kilpailu.enddate > CURRENT_TIMESTAMP"
					" ORDER BY Kilpailu.startdate")
		res = db.engine.execute(stmt)
		
		response = []
		for row in res:
			response.append({"luokkanimi":row[0],"kilpailunimi":row[1], "kilpailualkupaivamaara":row[2], "kilpailuloppupaivamaara":row[3]})

		return response
	
	# Metodi kilpailujen hakemista varten, johon liitetty tieto luokan nimestä -> Kilpailut-sivulle
	@staticmethod
	def kaikkiKilpailut():
		stmt = text("SELECT Luokka.name, Kilpailu.name, Kilpailu.venue, Kilpailu.startdate, Kilpailu.enddate, Kilpailu.id FROM Kilpailu"
					" LEFT JOIN Luokka ON Luokka.id = Kilpailu.luokka_id")
		res = db.engine.execute(stmt)

		response = []
		for row in res:
			response.append({"luokkanimi":row[0],"kilpailunimi":row[1],"kilpailupaikka":row[2],"kilpailualkupaivamaara":row[3],"kilpailuloppupaivamaara":row[4],"kilpailutunnus":row[5]})

		return response