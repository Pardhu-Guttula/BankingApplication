# Epic Title: Display Personalized Banking Products

from datetime import datetime
from backend.database import db

class BankingProduct(db.Model):
    __tablename__ = 'banking_products'
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(255), nullable=False)
    eligibility_criteria: str = db.Column(db.Text, nullable=False)
    created_at: datetime = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at: datetime = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)