# Epic Title: Create User Table in PostgreSQL

from sqlalchemy import Column, Integer, String
from backend.database.config import Base
from werkzeug.security import generate_password_hash

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=50), nullable=False)
    email = Column(String(length=100), unique=True, nullable=False)
    password_hash = Column(String(length=255), nullable=False)

    def set_password(self, password: str):
        self.password_hash = generate_password_hash(password)