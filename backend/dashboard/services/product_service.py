# Epic Title: Display Banking Products Dynamically

from backend.dashboard.repositories.product_repository import ProductRepository
from backend.dashboard.models.user_profile_model import UserProfile, BankingProduct

class ProductService:

    @staticmethod
    def fetch_dynamic_products(user_id: int) -> dict:
        user_profile: UserProfile = ProductRepository.get_user_profile(user_id)
        if not user_profile:
            return {'error': 'User profile not found'}

        products: List[BankingProduct] = ProductRepository.get_relevant_products(user_profile.eligibility_criteria)

        product_details = [{'name': product.name, 'description': product.description} for product in products]

        return {
            'user_id': user_profile.user_id,
            'products': product_details
        }