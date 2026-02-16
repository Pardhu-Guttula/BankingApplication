# Epic Title: Design User Profile-Based Dashboard

from typing import Dict, Any
from backend.dashboard.models.user_profile_model import db, UserProfile

class DashboardService:

    @staticmethod
    def get_dashboard_content(user_id: int) -> Dict[str, Any]:
        user_profile = UserProfile.query.filter_by(user_id=user_id).first()
        
        if not user_profile:
            return {'error': 'User not found'}

        content = {
            'user_name': user_profile.name,
            'recommended_products': DashboardService.get_recommended_products(user_profile)
        }
        
        return content

    @staticmethod
    def get_recommended_products(user_profile: UserProfile) -> list:
        # Placeholder logic for product recommendation based on user profile
        # In real application, actual logic or an external service should be used
        return user_profile.favorite_products.split(',') if user_profile.favorite_products else []