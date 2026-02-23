# Epic Title: Sort Products by Price

from sqlalchemy.orm import Session
from sqlalchemy import asc, desc
from backend.product_catalog.models.product import Product
from typing import List

class ProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_products_sorted_by_price(self, sort_order: str) -> List[Product]:
        if sort_order == 'asc':
            return self.db.query(Product).order_by(asc(Product.price)).all()
        elif sort_order == 'desc':
            return self.db.query(Product).order_by(desc(Product.price)).all()
        return self.db.query(Product).all()