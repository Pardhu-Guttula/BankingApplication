# Epic Title: Implement Multi-Factor Authentication

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class MFA(db.Model):
    __tablename__ = 'mfa'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    mfa_type = db.Column(db.String(50), nullable=False)
    mfa_secret = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean, default=True)