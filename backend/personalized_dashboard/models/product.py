# Epic Title: Display Personalized Banking Products

from backend.database import db

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    eligibility_criteria = db.Column(db.Text, nullable=False)  # JSON containing criteria