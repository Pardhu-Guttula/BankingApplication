# Epic Title: Display Banking Products Dynamically

from backend.dashboard.repositories.product_repository import ProductRepository
from backend.dashboard.models.product_model import UserProfile, Product, Offer

class ProductService:

    @staticmethod
    def get_dynamic_products(user_id: int) -> dict:
        user_profile = ProductRepository.get_user_profile(user_id)
        if not user_profile:
            return {}

        eligible_products = ProductRepository.get_eligible_products(user_profile)
        products_with_offers = []
        for product in eligible_products:
            offers = ProductRepository.get_active_offers(product.id)
            products_with_offers.append({
                'name': product.name,
                'description': product.description,
                'offers': [{'details': offer.offer_details} for offer in offers]
            })

        return {
            'user_profile': {
                'name': user_profile.name,
                'email': user_profile.email,
                'age': user_profile.age,
                'income': user_profile.income,
                'account_type': user_profile.account_type
            },
            'products': products_with_offers
        }