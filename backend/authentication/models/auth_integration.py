# Epic Title: Integrate Authentication with Bank Security Infrastructure

from datetime import datetime
from backend.database import db

class AuthIntegration(db.Model):
    __tablename__ = 'auth_integrations'
    id: int = db.Column(db.Integer, primary_key=True)
    integration_name: str = db.Column(db.String(255), nullable=False)
    integration_details: str = db.Column(db.Text, nullable=False)
    created_at: datetime = db.Column(db.DateTime, default=datetime.utcnow)