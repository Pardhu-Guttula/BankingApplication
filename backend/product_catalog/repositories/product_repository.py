# Epic Title: Display Product Details

from sqlalchemy.orm import Session
from backend.product_catalog.models.product import Product
from typing import Optional

class ProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_product_by_id(self, product_id: int) -> Optional[Product]:
        return self.db.query(Product).filter(Product.id == product_id).first()