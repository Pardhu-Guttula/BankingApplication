# Epic Title: Display Personalized Banking Products

import json
from backend.personalized_dashboard.repositories.user_profile_repository import UserProfileRepository
from backend.personalized_dashboard.repositories.product_repository import ProductRepository

class DashboardService:
    def __init__(self):
        self.user_profile_repository = UserProfileRepository()
        self.product_repository = ProductRepository()

    def get_personalized_dashboard(self, user_id: int) -> dict:
        user_profile = self.user_profile_repository.get_user_profile(user_id)
        if not user_profile:
            return {"message": "User profile not found"}

        products = self.product_repository.get_all_products()
        personalized_products = self.filter_products_by_eligibility(products, user_profile)
        
        return {
            "user_profile": user_profile,
            "personalized_products": personalized_products
        }

    def filter_products_by_eligibility(self, products: list, user_profile) -> list:
        eligible_products = []
        for product in products:
            criteria = json.loads(product.eligibility_criteria)
            if self.is_user_eligible(criteria, user_profile):
                eligible_products.append({
                    "id": product.id,
                    "name": product.name,
                    "description": product.description
                })
        return eligible_products

    def is_user_eligible(self, criteria: dict, user_profile) -> bool:
        if 'age' in criteria and not (criteria['age']['min'] <= user_profile.age <= criteria['age']['max']):
            return False
        if 'income' in criteria and not (criteria['income']['min'] <= user_profile.income <= criteria['income']['max']):
            return False
        if 'risk_tolerance' in criteria and user_profile.risk_tolerance not in criteria['risk_tolerance']:
            return False
        return True