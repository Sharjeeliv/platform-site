# Third-party imports
from flask_login import UserMixin
from sqlalchemy.sql import func

# Local Imports
from platform_site import db


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))             # Name of Project    
    description = db.Column(db.String(256))     # Description of Project
    github = db.Column(db.String(256))          # Github Repository
    link = db.Column(db.String(256))            # Project Link
    type = db.Column(db.String(32))             # Type of Project
    main = db.Column(db.String(32))             # Main Language
    langtools = db.Column(db.String(256))       # Language and Tools  
    datetime_added = db.Column(db.DateTime(timezone=True), default=func.now())


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(128))
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))