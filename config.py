import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
app = Flask(__name__)
SQLALCHEMY_DATABASE_URI = 'postgresql:///Fyyur'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_object('config')
db = SQLAlchemy(app)

#connect to db
migrate = Migrate(app, db)
# TODO: connect to a local postgresql database


# TODO IMPLEMENT DATABASE URL
