# Epic Title: Display Banking Products Dynamically

from typing import List, Dict
from backend.dashboard.models.product_model import db, Product
from backend.dashboard.models.user_profile_model import UserProfile

class ProductService:

    @staticmethod
    def get_products_for_user(user_id: int) -> List[Dict[str, str]]:
        user_profile = UserProfile.query.filter_by(user_id=user_id).first()
        
        if not user_profile:
            return [{'error': 'User not found'}]

        return ProductService._filter_products_based_on_profile(user_profile)

    @staticmethod
    def _filter_products_based_on_profile(user_profile: UserProfile) -> List[Dict[str, str]]:
        # Placeholder logic for product filtering based on user profile
        # In real application, actual logic or an external service should be used
        products = Product.query.all()
        filtered_products = [product for product in products if ProductService._is_product_suitable(product, user_profile)]
        
        return [{'name': product.name, 'category': product.category} for product in filtered_products]

    @staticmethod
    def _is_product_suitable(product: Product, user_profile: UserProfile) -> bool:
        # Placeholder eligibility check; should be replaced with actual logic
        return True