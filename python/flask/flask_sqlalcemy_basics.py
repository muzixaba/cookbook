"""
ORM used with Flask
"""
from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create instance of flask app & set configs
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"  # rel import
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# instanciate the db
db = SQLAlchemy(app)


# Models are tables in db
class User(db.Model):
    id = db.Column(db.Integer, primary=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)
    date_joined = db.Column(db.Date, default=datetime.utcnow)


# Flask-Migrate
# Add migrations
flask db migrate -m "message"
flask db upgrate (applies migrations)
flask db history (log of applied migrations)
flask db current (shows the last migration that was applied)