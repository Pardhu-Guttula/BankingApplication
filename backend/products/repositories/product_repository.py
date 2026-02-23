# Epic Title: Create Products Table in PostgreSQL

from sqlalchemy.orm import Session
from backend.products.models.product import Product
from typing import Optional

class ProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_product(self, name: str, price: float) -> Product:
        db_product = Product(name=name, price=price)
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product

    def get_product_by_id(self, product_id: int) -> Optional[Product]:
        return self.db.query(Product).filter(Product.id == product_id).first()

    def get_product_by_name(self, name: str) -> Optional[Product]:
        return self.db.query(Product).filter(Product.name == name).first()