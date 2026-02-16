# Epic Title: Display Banking Products Dynamically

from backend.dashboard.models.product_model import db, UserProfile, Product, Offer

class ProductRepository:

    @staticmethod
    def get_user_profile(user_id: int) -> UserProfile:
        return UserProfile.query.filter_by(user_id=user_id).first()

    @staticmethod
    def get_eligible_products(user_profile: UserProfile) -> list[Product]:
        all_products = Product.query.all()
        return [
            product for product in all_products
            if ProductRepository.is_user_eligible(user_profile, product.eligibility_criteria)
        ]

    @staticmethod
    def is_user_eligible(user_profile: UserProfile, criteria: str) -> bool:
        if criteria == "high_income" and user_profile.income > 50000:
            return True
        if criteria == "premium_account" and user_profile.account_type == "premium":
            return True
        return False

    @staticmethod
    def get_active_offers(product_id: int) -> list[Offer]:
        return Offer.query.filter_by(product_id=product_id, active=True).all()