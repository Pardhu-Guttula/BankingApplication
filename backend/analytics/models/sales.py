# Epic Title: Track Sales Performance Metrics

from sqlalchemy import Column, Integer, Float, Date, String
from backend.database.config import Base

class Sales(Base):
    __tablename__ = 'sales'

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)
    amount = Column(Float, nullable=False)
    category = Column(String, nullable=False)
    product_id = Column(Integer, nullable=False)