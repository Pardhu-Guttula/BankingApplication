# Epic Title: Create Products Table in PostgreSQL

from sqlalchemy.orm import Session
from backend.products.repositories.product_repository import ProductRepository
from backend.products.models.product import Product

class ProductService:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def add_product(self, db: Session, name: str, price: float) -> Product:
        if price <= 0:
            raise ValueError("Price must be a positive value")

        if self.product_repository.get_product_by_name(name):
            raise ValueError(f"Product with name {name} already exists")

        new_product = self.product_repository.create_product(name, price)
        return new_product