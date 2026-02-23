# Epic Title: Filter Products by Category

from sqlalchemy.orm import Session
from backend.product_catalog.repositories.category_repository import CategoryRepository
from backend.product_catalog.models.category import Category

class CategoryService:
    def __init__(self, category_repository: CategoryRepository):
        self.category_repository = category_repository

    def fetch_all_categories(self, db: Session) -> List[Category]:
        return self.category_repository.get_all_categories()

    def fetch_category_by_id(self, db: Session, category_id: int) -> Category:
        return self.category_repository.get_category_by_id(category_id)