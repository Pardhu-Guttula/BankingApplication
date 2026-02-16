# Epic Title: Implement Data Encryption Protocols

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class EncryptionKey(db.Model):
    __tablename__ = 'encryption_keys'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False, unique=True)
    key = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)