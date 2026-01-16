from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Dessert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Integer)
    description = db.Column(db.Text)
    image_url = db.Column(db.String(255))
    category = db.Column(db.String(50))

