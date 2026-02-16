# Epic Title: Implement Account Lockout Mechanism

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class FailedLoginAttempt(db.Model):
    __tablename__ = 'failed_login_attempts'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

class AccountLockout(db.Model):
    __tablename__ = 'account_lockouts'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    lockout_time = db.Column(db.DateTime, default=datetime.utcnow)
    lockout_duration = db.Column(db.Integer, nullable=False) # Duration in minutes