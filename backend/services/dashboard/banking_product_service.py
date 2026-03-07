# Epic Title: Banking Platform — Core API

from backend.repositories.dashboard.banking_product_repository import BankingProductRepository
from backend.models.dashboard.banking_product import BankingProduct

class BankingProductService:
    def __init__(self):
        self.repository = BankingProductRepository()

    def add_banking_product(self, product_id: str, name: str, description: str, eligibility_criteria: str):
        product = BankingProduct(product_id, name, description, eligibility_criteria)
        self.repository.save_banking_product(product)
        return product

    def get_all_products(self) -> list:
        return self.repository.get_all_banking_products()

    def get_eligible_products(self, eligibility_criteria: str) -> list:
        return self.repository.get_eligible_products(eligibility_criteria)

    def get_product_details(self, product_id: str) -> BankingProduct:
        return self.repository.get_product_details(product_id)