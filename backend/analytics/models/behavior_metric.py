# Epic Title: Monitor User Behavior Metrics

from sqlalchemy import Column, Integer, String, DateTime, Float
from backend.database.config import Base
from datetime import datetime

class BehaviorMetric(Base):
    __tablename__ = 'behavior_metrics'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    session_duration = Column(Float, nullable=True)
    page_views = Column(Integer, nullable=True)
    click_through_rate = Column(Float, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)