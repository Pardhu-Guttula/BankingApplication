# Epic Title: Display Personalized Banking Products

from backend.database import db

class UserProfile(db.Model):
    __tablename__ = 'user_profiles'
    user_id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(100), nullable=False)
    email: str = db.Column(db.String(100), unique=True, nullable=False)
    age: int = db.Column(db.Integer, nullable=False)
    income_bracket: str = db.Column(db.String(50), nullable=False)
    preferences: str = db.Column(db.String(255))