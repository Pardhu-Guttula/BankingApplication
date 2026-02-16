# Epic Title: Design User Profile-Based Dashboard

from backend.dashboard.models.dashboard_model import db, UserProfile, ProductService

class DashboardRepository:

    @staticmethod
    def get_user_profile(user_id: int) -> UserProfile:
        return UserProfile.query.filter_by(user_id=user_id).first()

    @staticmethod
    def get_eligible_products(user_profile: UserProfile) -> list[ProductService]:
        eligible_products = ProductService.query.all()
        return [
            product for product in eligible_products
            if DashboardRepository.is_user_eligible(user_profile, product.eligibility_criteria)
        ]

    @staticmethod
    def is_user_eligible(user_profile: UserProfile, criteria: str) -> bool:
        # Simplified criteria check for demonstration
        if criteria == "high_income" and user_profile.income > 50000:
            return True
        if criteria == "premium_account" and user_profile.account_type == "premium":
            return True
        return False