# Epic Title: Implement Account Lockout Mechanism

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class LoginAttempt(db.Model):
    __tablename__ = 'login_attempts'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    success = db.Column(db.Boolean, nullable=False, default=False)