# Epic Title: Implement user authentication and authorization features

from backend.authentication.models.user import User
from typing import Optional

class UserRepository:
    def __init__(self):
        self._users = [
            User(1, "John Doe", "john@example.com", User.hash_password("password123"))
        ]

    def find_by_email(self, email: str) -> Optional[User]:
        for user in self._users:
            if user.email == email:
                return user
        return None