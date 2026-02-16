# Epic Title: Display Personalized Banking Products

from backend.database import db

class Product(db.Model):
    __tablename__ = 'products'
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(100), nullable=False)
    eligibility_criteria: str = db.Column(db.String(255), nullable=False)
    recommended_for: str = db.Column(db.String(255), nullable=False)