
from app import db

class User(db.Model):
    __tablename__ = 'users'
    name = db.Column(db.String())
    surname = db.Column(db.String())
