# Epic Title: Display Personalized Banking Products

from backend.personalized_dashboard.models.user_profile import UserProfile

class UserProfileRepository:

    def get_user_profile(self, user_id: int) -> UserProfile:
        return UserProfile.query.filter_by(user_id=user_id).first()