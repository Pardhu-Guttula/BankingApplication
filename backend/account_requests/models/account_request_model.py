# Epic Title: Simplify Account Opening Workflow

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class AccountRequest(db.Model):
    __tablename__ = 'account_requests'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), nullable=False, default='Pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)