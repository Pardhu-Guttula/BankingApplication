# Epic Title: Implement user authentication and authorization features

from backend.access_control.repositories.role_repository import RoleRepository
from backend.access_control.repositories.user_repository import UserRepository

class RoleService:
    def __init__(self, role_repository: RoleRepository, user_repository: UserRepository):
        self.role_repository = role_repository
        self.user_repository = user_repository

    def assign_role(self, user_email: str, role_name: str) -> bool:
        user = self.user_repository.find_by_email(user_email)
        role = self.role_repository.get_role_by_name(role_name)
        if user and role:
            self.user_repository.update_role(user.user_id, role.role_id)
            return True
        return False

    def get_permissions(self, user_email: str) -> list:
        user = self.user_repository.find_by_email(user_email)
        if user:
            role = self.role_repository.get_role_by_name(user.role_id)
            return role.permissions if role else []
        return []