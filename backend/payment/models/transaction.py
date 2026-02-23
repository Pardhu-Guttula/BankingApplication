# Epic Title: Integrate Payment Gateway (Stripe) for Processing Payments

from sqlalchemy import Column, Integer, String, Float, DateTime
from backend.database.config import Base
from datetime import datetime

class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    transaction_id = Column(String, nullable=False, unique=True)
    amount = Column(Float, nullable=False)
    status = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)