# Epic Title: Save and Resume Incomplete Applications

from datetime import datetime
from backend.database import db

class Application(db.Model):
    __tablename__ = 'applications'
    id: int = db.Column(db.Integer, primary_key=True)
    user_id: int = db.Column(db.Integer, nullable=False)
    application_data: str = db.Column(db.Text, nullable=False)  # JSON string containing application data
    created_at: datetime = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at: datetime = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)