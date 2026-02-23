# Epic Title: Update Personal Information

from sqlalchemy.orm import Session
from backend.user_profile.models.user_profile import UserProfile

class UserProfileRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_user_profile_by_user_id(self, user_id: int) -> UserProfile:
        return self.db.query(UserProfile).filter(UserProfile.user_id == user_id).first()

    def update_user_profile(self, user_id: int, first_name: str, last_name: str, email: str, phone_number: str, address: str) -> UserProfile:
        user_profile = self.get_user_profile_by_user_id(user_id)
        if user_profile:
            user_profile.first_name = first_name
            user_profile.last_name = last_name
            user_profile.email = email
            user_profile.phone_number = phone_number
            user_profile.address = address
            self.db.commit()
            self.db.refresh(user_profile)
        return user_profile