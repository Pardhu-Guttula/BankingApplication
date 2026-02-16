# Epic Title: Implement Multi-Factor Authentication

from datetime import datetime, timedelta
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class MFA(db.Model):
    __tablename__ = 'mfa'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False, unique=True)
    mfa_code = db.Column(db.String(6), nullable=False)
    method = db.Column(db.String(50), nullable=False)  # SMS, Email, App
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    expires_at = db.Column(db.DateTime, default=datetime.utcnow() + timedelta(minutes=5))

    def is_expired(self) -> bool:
        return datetime.utcnow() > self.expires_at