# Epic Title: Display Banking Products Dynamically

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    eligibility_criteria = db.Column(db.String(500), nullable=True)  # Placeholder for eligibility logic
    created_at = db.Column(db.DateTime, default=datetime.utcnow)