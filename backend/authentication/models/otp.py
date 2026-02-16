# Epic Title: Implement Multi-Factor Authentication (MFA)

from datetime import datetime
from backend.database import db

class OTP(db.Model):
    __tablename__ = 'otps'
    id: int = db.Column(db.Integer, primary_key=True)
    user_id: int = db.Column(db.Integer, nullable=False)
    otp_code: str = db.Column(db.String(6), nullable=False)
    expires_at: datetime = db.Column(db.DateTime, nullable=False)
    created_at: datetime = db.Column(db.DateTime, default=datetime.utcnow)