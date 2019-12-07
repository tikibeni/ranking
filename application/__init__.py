from flask import Flask
app = Flask(__name__)

# Tietokanta ja Heroku
from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ranking.db"
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

# Elementtien tuominen yhteen
from application import views

from application.auth import models
from application.auth import views

from application.luokat import models
from application.luokat import views

from application.tulokset import models

from application.kilpailut import models
from application.kilpailut import views

from application.kilpailijat import models
from application.kilpailijat import views

# Kirjautuminen
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager, current_user
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Kirjaudu sisään käyttääksesi tätä."

# Roolit
from functools import wraps

## Login_requiredin määrittäminen siten, että se vaatii admin-oikeudet.
def login_required(role="admin"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user:
                return login_manager.unauthorized()

            if not current_user.is_authenticated:
                return login_manager.unauthorized()

            unauthorized = False

            if role != "admin":
                unauthorized = True

                for user_role in current_user.roles():
                    if user_role == role:
                        unauthorized = False
                        break

            if unauthorized:
                return login_manager.unauthorized()

            return fn(*args, **kwargs)
        return decorated_view
    return wrapper

# Lisää kirjautumisesta
from application.auth.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

try:
    db.create_all()
except:
    pass