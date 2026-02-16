# Epic Title: Streamline Service Modification Requests

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ServiceModificationRequest(db.Model):
    __tablename__ = 'service_modification_requests'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    service_id = db.Column(db.Integer, nullable=False)
    modification_details = db.Column(db.String(255), nullable=False)
    request_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(50), nullable=False)