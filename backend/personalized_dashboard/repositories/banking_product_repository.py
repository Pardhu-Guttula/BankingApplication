# Epic Title: Display Personalized Banking Products

from backend.personalized_dashboard.models.banking_product import BankingProduct
from backend.database import db

class BankingProductRepository:

    def get_all_products(self) -> list[BankingProduct]:
        return BankingProduct.query.all()