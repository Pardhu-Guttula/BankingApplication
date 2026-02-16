# Epic Title: Design User Profile-Based Dashboard

from typing import Optional
from backend.dashboard.models.user_profile_model import db, UserProfile

class UserProfileRepository:

    @staticmethod
    def get_user_profile(user_id: int) -> Optional[UserProfile]:
        return UserProfile.query.filter_by(user_id=user_id).first()