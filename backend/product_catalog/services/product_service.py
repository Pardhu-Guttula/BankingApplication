# Epic Title: Sort Products by Price

from sqlalchemy.orm import Session
from backend.product_catalog.repositories.product_repository import ProductRepository
from backend.product_catalog.models.product import Product
from typing import List

class ProductService:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def fetch_sorted_products(self, db: Session, sort_order: str) -> List[Product]:
        return self.product_repository.get_products_sorted_by_price(sort_order)