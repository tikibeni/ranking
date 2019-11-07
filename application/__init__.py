# Flask käyttöön
from flask import Flask
app = Flask(__name__)

# SQLAlchemy käyttöön
from flask_sqlalchemy import SQLAlchemy

# Käytetään tasks.db nimistä SQLite-tietokantaa.
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"

# Pyydetään SQLAlchemyä tulostamaan kaikki kyselyt
app.config["SQLALCHEMY_ECHO"] = True

# Luodaan db-olio, jota käytetään tietokannan käsittelyyn
db = SQLAlchemy(app)

# Luetaan kansiosta application tiedoston views sisältö
from application import views

# Kansiosta tasks models sisältö
from application.tasks import models

# Kansiosta tasks views sisältö
from application.tasks import views

# Luodaan lopulta tarvittavat tietokantataulut
db.create_all()
