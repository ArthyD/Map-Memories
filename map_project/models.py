from sqlalchemy.sql import func
from . import db

class ImageServer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    lat = db.Column(db.Float)
    long = db.Column(db.Float)
    path = db.Column(db.String(512))
    comment = db.Column(db.String(1024))