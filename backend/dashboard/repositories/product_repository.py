# Epic Title: Display Banking Products Dynamically

from typing import List
from backend.dashboard.models.product_model import db, Product

class ProductRepository:

    @staticmethod
    def get_all_products() -> List[Product]:
        return Product.query.all()