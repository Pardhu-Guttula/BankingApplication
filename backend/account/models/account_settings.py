# Epic Title: Manage Account

from sqlalchemy import Column, Integer, String, Boolean, DateTime
from backend.database.config import Base
from datetime import datetime

class AccountSettings(Base):
    __tablename__ = 'account_settings'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False, unique=True)
    email_notifications = Column(Boolean, default=True)
    sms_notifications = Column(Boolean, default=True)
    dark_mode = Column(Boolean, default=False)
    privacy_settings = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)