# Epic Title: Display Product Details

from sqlalchemy.orm import Session
from backend.product_catalog.repositories.product_repository import ProductRepository
from backend.product_catalog.models.product import Product
from typing import Union

class ProductService:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def fetch_product_details(self, db: Session, product_id: int) -> Union[Product, str]:
        product = self.product_repository.get_product_by_id(product_id)
        if product:
            return product
        return "Product details are not available"