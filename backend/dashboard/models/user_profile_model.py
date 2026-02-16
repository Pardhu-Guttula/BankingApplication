# Epic Title: Design User Profile-Based Dashboard

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UserProfile(db.Model):
    __tablename__ = 'user_profiles'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    preferences = db.Column(db.String(255), nullable=True)
    eligibility_criteria = db.Column(db.String(255), nullable=True)

class BankingProduct(db.Model):
    __tablename__ = 'banking_products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    eligibility = db.Column(db.String(255), nullable=False)