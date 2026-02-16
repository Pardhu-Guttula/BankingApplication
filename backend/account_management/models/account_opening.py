# Epic Title: Enable Account Opening Requests

from datetime import datetime
from backend.database import db

class AccountOpeningRequest(db.Model):
    __tablename__ = 'account_opening_requests'
    id: int = db.Column(db.Integer, primary_key=True)
    user_id: int = db.Column(db.Integer, nullable=False)
    account_type: str = db.Column(db.String(50), nullable=False)
    created_at: datetime = db.Column(db.DateTime, default=datetime.utcnow)
    status: str = db.Column(db.String(20), nullable=False, default='pending')