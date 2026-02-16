# Epic Title: Display Banking Products Dynamically

from typing import List
from backend.dashboard.models.user_profile_model import db, UserProfile, BankingProduct

class ProductRepository:

    @staticmethod
    def get_user_profile(user_id: int) -> UserProfile:
        return UserProfile.query.filter_by(user_id=user_id).first()

    @staticmethod
    def get_relevant_products(eligibility_criteria: str) -> List[BankingProduct]:
        return BankingProduct.query.filter(BankingProduct.eligibility.contains(eligibility_criteria)).all()