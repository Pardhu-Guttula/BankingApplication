# Epic Title: Filter Products by Category

from sqlalchemy.orm import Session
from backend.product_catalog.models.category import Category
from typing import List, Optional

class CategoryRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all_categories(self) -> List[Category]:
        return self.db.query(Category).all()

    def get_category_by_id(self, category_id: int) -> Optional[Category]:
        return self.db.query(Category).filter(Category.id == category_id).first()