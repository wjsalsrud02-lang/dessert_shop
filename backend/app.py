from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import db, Dessert

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"

db.init_app(app)

with app.app_context():
    db.create_all()
    
@app.route("/api/desserts")
def get_desserts():
    desserts = Dessert.query.all()
    return jsonify([
        {
            "id": d.id,
            "name": d.name,
            "price": d.price,
            "description": d.description,
            "image_url": d.image_url,
            "category": d.category
        } for d in desserts
    ])

if __name__ == "__main__":
    app.run(debug=True)
