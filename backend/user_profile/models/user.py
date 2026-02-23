# Epic Title: Ensure Secure Storage and Retrieval

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.hybrid import hybrid_property
from backend.database.config import Base
from datetime import datetime
from cryptography.fernet import Fernet
import os

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False, unique=True)
    _hashed_password = Column('hashed_password', String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    @hybrid_property
    def hashed_password(self):
        return Fernet(User._get_fernet_key()).decrypt(self._hashed_password.encode()).decode()

    @hashed_password.setter
    def hashed_password(self, password: str):
        self._hashed_password = Fernet(User._get_fernet_key()).encrypt(password.encode()).decode()

    @staticmethod
    def _get_fernet_key():
        return os.getenv('FERNET_KEY').encode()