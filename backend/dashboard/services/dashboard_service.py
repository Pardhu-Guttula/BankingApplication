# Epic Title: Design User Profile-Based Dashboard

from backend.dashboard.repositories.dashboard_repository import DashboardRepository
from backend.dashboard.models.dashboard_model import UserProfile, ProductService

class DashboardService:

    @staticmethod
    def get_personalized_dashboard(user_id: int) -> dict:
        user_profile = DashboardRepository.get_user_profile(user_id)
        if not user_profile:
            return {}

        eligible_products = DashboardRepository.get_eligible_products(user_profile)
        return {
            'user_profile': {
                'name': user_profile.name,
                'email': user_profile.email,
                'age': user_profile.age,
                'income': user_profile.income,
                'account_type': user_profile.account_type
            },
            'eligible_products': [
                {
                    'name': product.name,
                    'description': product.description
                } for product in eligible_products
            ]
        }