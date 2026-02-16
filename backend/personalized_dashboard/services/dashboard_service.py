# Epic Title: Display Personalized Banking Products

from backend.personalized_dashboard.repositories.user_profile_repository import UserProfileRepository
from backend.personalized_dashboard.repositories.product_repository import ProductRepository

class DashboardService:
    def __init__(self):
        self.user_profile_repository = UserProfileRepository()
        self.product_repository = ProductRepository()

    def get_user_dashboard(self, user_id: int) -> dict:
        user_profile = self.user_profile_repository.get_user_profile(user_id)
        all_products = self.product_repository.get_all_products()

        personalized_products = []
        for product in all_products:
            if self._matches_criteria(user_profile, product):
                personalized_products.append({
                    'id': product.id,
                    'name': product.name
                })

        return {
            'user': {
                'name': user_profile.name,
                'email': user_profile.email,
                'age': user_profile.age,
                'income_bracket': user_profile.income_bracket,
                'preferences': user_profile.preferences
            },
            'personalized_products': personalized_products
        }

    def _matches_criteria(self, user_profile, product):
        # Simplified criteria check for demonstration purposes
        if product.eligibility_criteria in user_profile.preferences:
            return True
        return False