# Epic Title: Implement Multi-Factor Authentication (MFA)

from datetime import datetime
from backend.database import db

class MFA(db.Model):
    __tablename__ = 'mfa_tokens'
    id: int = db.Column(db.Integer, primary_key=True)
    user_id: int = db.Column(db.Integer, nullable=False)
    otp: str = db.Column(db.String(6), nullable=False)
    method: str = db.Column(db.String(10), nullable=False)  # email, sms, biometric
    created_at: datetime = db.Column(db.DateTime, default=datetime.utcnow)
    expires_at: datetime = db.Column(db.DateTime, nullable=False)