# Epic Title: Ensure Secure Storage and Retrieval

from sqlalchemy.orm import Session
from backend.user_profile.models.user import User

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_user_by_id(self, user_id: int) -> User:
        return self.db.query(User).filter(User.id == user_id).first()

    def update_user_password(self, user_id: int, new_password: str) -> User:
        user = self.get_user_by_id(user_id)
        if user:
            user.hashed_password = new_password
            self.db.commit()
            self.db.refresh(user)
        return user