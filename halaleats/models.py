# Third-party imports
from flask_login import UserMixin
from sqlalchemy.sql import func

# Local Imports
from halaleats import db


class Eatery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    address = db.Column(db.String(256), unique=True)
    cuisine = db.Column(db.String(32))
    verification_type = db.Column(db.String(32))
    certificate_file = db.Column(db.String(32))
    alcohol_served = db.Column(db.Boolean)
    datetime_added = db.Column(db.DateTime(timezone=True), default=func.now())


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(128))
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))