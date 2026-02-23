# Epic Title: Update Personal Information

from sqlalchemy.orm import Session
from backend.user_profile.repositories.user_profile_repository import UserProfileRepository
from backend.user_profile.models.user_profile import UserProfile

class UserProfileService:
    def __init__(self, user_profile_repository: UserProfileRepository):
        self.user_profile_repository = user_profile_repository

    def update_user_profile(self, db: Session, user_id: int, first_name: str, last_name: str, email: str, phone_number: str, address: str) -> UserProfile:
        user_profile = self.user_profile_repository.update_user_profile(user_id, first_name, last_name, email, phone_number, address)
        return user_profile