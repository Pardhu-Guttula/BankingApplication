# Epic Title: Change Password

from sqlalchemy.orm import Session
from backend.user_profile.repositories.user_repository import UserRepository
from backend.user_profile.models.user import User
from werkzeug.security import check_password_hash, generate_password_hash

class UserService:
    PASSWORD_COMPLEXITY_ERROR = "Password must be at least 8 characters long and include at least one special character."

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def validate_password_complexity(self, password: str) -> bool:
        if len(password) < 8 or not any(char in "!@#$%^&*()" for char in password):
            return False
        return True

    def change_password(self, db: Session, user_id: int, old_password: str, new_password: str) -> dict:
        user = self.user_repository.get_user_by_id(user_id)
        if user and check_password_hash(user.hashed_password, old_password):
            if self.validate_password_complexity(new_password):
                new_hashed_password = generate_password_hash(new_password)
                self.user_repository.update_user_password(user_id, new_hashed_password)
                return {"success": True}
            return {"success": False, "error": self.PASSWORD_COMPLEXITY_ERROR}
        return {"success": False, "error": "Incorrect existing password"}