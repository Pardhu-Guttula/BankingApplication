# Epic Title: Remove Products from the Shopping Cart

from sqlalchemy import Column, Integer, ForeignKey
from backend.database.config import Base

class Cart(Base):
    __tablename__ = 'carts'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)