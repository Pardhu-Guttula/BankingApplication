# Epic Title: Create Orders Table in PostgreSQL

from sqlalchemy import Column, Integer, Float, ForeignKey
from backend.database.config import Base

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    total_amount = Column(Float, nullable=False)