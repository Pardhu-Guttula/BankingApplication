# Epic Title: Implement user authentication and authorization features

from typing import List, Optional
from backend.access_control.models.user import User

class UserRepository:
    def __init__(self):
        self.users = [
            User(1, "John Doe", "john@example.com", 2)
        ]

    def find_by_email(self, email: str) -> Optional[User]:
        for user in self.users:
            if user.email == email:
                return user
        return None

    def update_role(self, user_id: int, role_id: int) -> bool:
        for user in self.users:
            if user.user_id == user_id:
                user.role_id = role_id
                return True
        return False