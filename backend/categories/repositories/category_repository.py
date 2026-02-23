# Epic Title: Create Categories Table in PostgreSQL

from sqlalchemy.orm import Session
from backend.categories.models.category import Category
from typing import Optional

class CategoryRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_category(self, name: str, parent_category_id: Optional[int]) -> Category:
        db_category = Category(name=name, parent_category_id=parent_category_id)
        self.db.add(db_category)
        self.db.commit()
        self.db.refresh(db_category)
        return db_category

    def get_category_by_id(self, category_id: int) -> Optional[Category]:
        return self.db.query(Category).filter(Category.id == category_id).first()

    def get_category_by_name(self, name: str) -> Optional[Category]:
        return self.db.query(Category).filter(Category.name == name).first()