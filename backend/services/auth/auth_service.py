# Epic Title: Banking Platform — Core API

from backend.repositories.auth.user_repository import UserRepository
from backend.repositories.auth.role_repository import RoleRepository
from backend.models.auth.user import User

class AuthService:
    def __init__(self):
        self.user_repository = UserRepository()
        self.role_repository = RoleRepository()

    def get_user(self, user_id: str) -> User:
        return self.user_repository.get_user(user_id)

    def perform_authorized_action(self, user_id: str, required_permission: str) -> bool:
        user = self.get_user(user_id)
        for role in user.roles:
            permissions = self.role_repository.get_role_permissions(role)
            if required_permission in permissions:
                return True
        return False