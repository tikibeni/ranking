from application import db
from sqlalchemy import text

# Tulos-liitostaulun luominen
class Tulos(db.Model):
    __tablename__='liitostaulu'
    id = db.Column(db.Integer, primary_key=True)
    sijoitus = db.Column(db.Integer, nullable=False)
    pisteet = db.Column(db.Integer, nullable=False)
    
    kilpailu_id = db.Column(db.Integer, db.ForeignKey('kilpailu.id'), nullable=False)
    kilpailija_id = db.Column(db.Integer, db.ForeignKey('kilpailija.id'), nullable=False)

    def __init__(self, sijoitus, pisteet, kilpailu_id, kilpailija_id):
        self.sijoitus = sijoitus
        self.pisteet = pisteet
        self.kilpailu_id = kilpailu_id
        self.kilpailija_id = kilpailija_id

    def get_id(self):
        return self.id
    
    def get_kilpailuId(self):
        return self.kilpailu_id

    def get_kilpailijaId(self):
        return self.kilpailija_id


    # Metodi kilpailukohtaisten kilpailijatulosten hakemiseen Kilpailu.id:n avulla
    @staticmethod
    def kilpailunTulokset(tarkasteltavaKilpailuId):

        stmt = text("SELECT liitostaulu.sijoitus, Kilpailija.sailnumber, Kilpailija.name, Kilpailija.sailclub,"
                    " liitostaulu.pisteet, liitostaulu.id FROM liitostaulu"
                    " JOIN Kilpailija ON Kilpailija.id = liitostaulu.kilpailija_id"
                    " JOIN Kilpailu ON Kilpailu.id = liitostaulu.kilpailu_id"
                    " WHERE liitostaulu.kilpailu_id = :iidee"
                    " ORDER BY liitostaulu.sijoitus")
        res = db.engine.execute(stmt, iidee=tarkasteltavaKilpailuId)

        response = []
        for row in res:
            response.append({"sijoitus":row[0],"purjenumero":row[1],"nimi":row[2],"pursiseura":row[3],"pisteet":row[4],"id":row[5]})

        return response

    # Metodi tietyn kilpailun tietojen hakua varten
    @staticmethod
    def kilpailunTiedot(tarkasteltavaKilpailuId):

        stmt = text ("SELECT Luokka.name, Kilpailu.name, Kilpailu.venue FROM Kilpailu"
                    " JOIN Luokka ON Luokka.id = Kilpailu.luokka_id"
                    " WHERE Kilpailu.id = :iidee")
        res = db.engine.execute(stmt, iidee=tarkasteltavaKilpailuId)

        response = []
        for row in res:
            response.append({"luokka":row[0],"kilpnimi":row[1],"kilpaikka":row[2]})

        return response 