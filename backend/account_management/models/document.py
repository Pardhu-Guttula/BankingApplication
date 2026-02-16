# Epic Title: Upload Documentation for Account Requests

from datetime import datetime
from backend.database import db

class Document(db.Model):
    __tablename__ = 'documents'
    id: int = db.Column(db.Integer, primary_key=True)
    filename: str = db.Column(db.String(255), nullable=False)
    file_path: str = db.Column(db.String(255), nullable=False)
    uploaded_at: datetime = db.Column(db.DateTime, default=datetime.utcnow)