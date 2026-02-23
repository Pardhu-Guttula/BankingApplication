# Epic Title: Generate Detailed E-commerce Performance Reports

from sqlalchemy import Column, Integer, Float, DateTime, String
from backend.database.config import Base
from datetime import datetime

class Performance(Base):
    __tablename__ = 'performances'

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, nullable=False)
    metric_name = Column(String, nullable=False)
    metric_value = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)