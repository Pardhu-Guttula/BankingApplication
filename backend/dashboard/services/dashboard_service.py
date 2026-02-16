# Epic Title: Design User Profile-Based Dashboard

from backend.dashboard.repositories.dashboard_repository import DashboardRepository
from backend.dashboard.models.user_profile_model import UserProfile, BankingProduct

class DashboardService:

    @staticmethod
    def get_personalized_dashboard(user_id: int) -> dict:
        user_profile: UserProfile = DashboardRepository.get_user_profile(user_id)
        if not user_profile:
            return {'error': 'User profile not found'}

        products: List[BankingProduct] = DashboardRepository.get_relevant_products(user_profile.eligibility_criteria)

        product_details = [{'name': product.name, 'description': product.description} for product in products]

        return {
            'user_id': user_profile.user_id,
            'preferences': user_profile.preferences,
            'products': product_details
        }