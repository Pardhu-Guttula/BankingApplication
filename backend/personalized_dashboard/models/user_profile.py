# Epic Title: Display Personalized Banking Products

from datetime import datetime
from backend.database import db

class UserProfile(db.Model):
    __tablename__ = 'user_profiles'
    id: int = db.Column(db.Integer, primary_key=True)
    user_id: int = db.Column(db.Integer, unique=True, nullable=False)
    user_data: str = db.Column(db.Text, nullable=False)
    created_at: datetime = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at: datetime = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)