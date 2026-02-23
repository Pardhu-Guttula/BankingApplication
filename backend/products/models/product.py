# Epic Title: Create Products Table in PostgreSQL

from sqlalchemy import Column, Integer, String, Float
from backend.database.config import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=100), index=True, nullable=False)
    price = Column(Float, nullable=False)