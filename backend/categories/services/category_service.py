# Epic Title: Create Categories Table in PostgreSQL

from sqlalchemy.orm import Session
from backend.categories.repositories.category_repository import CategoryRepository
from backend.categories.models.category import Category

class CategoryService:
    def __init__(self, category_repository: CategoryRepository):
        self.category_repository = category_repository

    def add_category(self, db: Session, name: str, parent_category_id: Optional[int]) -> Category:
        if parent_category_id is not None:
            parent_category = self.category_repository.get_category_by_id(parent_category_id)
            if parent_category is None:
                raise ValueError("Invalid parent category ID")

        new_category = self.category_repository.create_category(name, parent_category_id)
        return new_category