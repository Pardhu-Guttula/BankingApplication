# Epic Title: Design User Profile-Based Dashboard

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UserProfile(db.Model):
    __tablename__ = 'user_profiles'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    income = db.Column(db.Float, nullable=False)
    account_type = db.Column(db.String(50), nullable=False)

class ProductService(db.Model):
    __tablename__ = 'product_services'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    eligibility_criteria = db.Column(db.String(255), nullable=False)