# Epic Title: Implement Account Lockout Mechanism

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class LockedAccount(db.Model):
    __tablename__ = 'locked_accounts'

    user_id = db.Column(db.Integer, primary_key=True)
    locked_until = db.Column(db.DateTime, nullable=False)