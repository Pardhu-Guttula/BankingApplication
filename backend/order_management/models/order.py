# Epic Title: Store Order Data in PostgreSQL

from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from backend.database.config import Base
from datetime import datetime

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(String, nullable=False, unique=True)
    user_id = Column(Integer, nullable=False)
    total_amount = Column(Float, nullable=False)
    transaction_id = Column(String, nullable=False, unique=True)
    status = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class OrderItem(Base):
    __tablename__ = 'order_items'

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    product_id = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)