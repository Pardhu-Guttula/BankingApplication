# Epic Title: Display Personalized Banking Products

from backend.personalized_dashboard.repositories.user_profile_repository import UserProfileRepository
from backend.personalized_dashboard.repositories.banking_product_repository import BankingProductRepository

class DashboardService:
    def __init__(self):
        self.user_profile_repository = UserProfileRepository()
        self.banking_product_repository = BankingProductRepository()

    def get_personalized_data(self, user_id: int) -> dict:
        user_profile = self.user_profile_repository.get_user_profile(user_id)
        products = self.banking_product_repository.get_all_products()

        personalized_products = [product for product in products if self._is_product_eligible(product, user_profile)]

        return {
            "user_profile": user_profile.user_data,
            "personalized_products": [product.name for product in personalized_products]
        }

    def _is_product_eligible(self, product, user_profile) -> bool:
        # Here you can add more complex eligibility criteria checks
        criteria = product.eligibility_criteria.lower()
        user_data = user_profile.user_data.lower()
        return criteria in user_data