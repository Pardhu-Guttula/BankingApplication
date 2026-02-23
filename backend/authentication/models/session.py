# Epic Title: Develop User Logout Capability

from sqlalchemy import Column, Integer, String, TIMESTAMP
from backend.database.config import Base

class Session(Base):
    __tablename__ = 'sessions'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    token = Column(String(length=255), unique=True, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    expires_at = Column(TIMESTAMP, nullable=False)