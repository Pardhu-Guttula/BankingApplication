# Epic Title: Create Categories Table in PostgreSQL

from sqlalchemy import Column, Integer, String, ForeignKey
from backend.database.config import Base

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=100), index=True, nullable=False)
    parent_category_id = Column(Integer, ForeignKey('categories.id'))