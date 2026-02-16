# Epic Title: Streamline Service Modification Requests

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class ServiceModificationRequest(db.Model):
    __tablename__ = 'service_modification_requests'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    service_id = db.Column(db.Integer, nullable=False)
    modification_type = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False, default='pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)