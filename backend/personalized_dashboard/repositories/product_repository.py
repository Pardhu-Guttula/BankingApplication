# Epic Title: Display Personalized Banking Products

from backend.personalized_dashboard.models.product import Product
from typing import List

class ProductRepository:

    def get_all_products(self) -> List[Product]:
        return Product.query.all()