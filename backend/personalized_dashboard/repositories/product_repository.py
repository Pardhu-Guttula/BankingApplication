# Epic Title: Display Personalized Banking Products

from backend.personalized_dashboard.models.product import Product

class ProductRepository:

    def get_all_products(self) -> list[Product]:
        return Product.query.all()