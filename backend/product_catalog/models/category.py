# Epic Title: Filter Products by Category

from sqlalchemy import Column, Integer, String
from backend.database.config import Base

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)