from flask import render_template
from application import app
from application.kilpailut.models import Kilpailu

@app.route("/")
def index():
	return render_template("index.html", tulevat_kisat=Kilpailu.tulevatKilpailut())