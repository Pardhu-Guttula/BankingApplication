# Epic Title: Banking Platform — Core API

from backend.repositories.auth.user_repository import UserRepository
from backend.models.auth.user import User

class UserService:
    def __init__(self):
        self.repository = UserRepository()

    def get_user(self, user_id: str) -> User:
        return self.repository.get_user(user_id)

    def assign_role(self, user_id: str, role_name: str) -> None:
        self.repository.assign_role(user_id, role_name)
        self.log_role_assignment(user_id, role_name)

    def revoke_role(self, user_id: str, role_name: str) -> None:
        self.repository.revoke_role(user_id, role_name)
        self.log_role_revocation(user_id, role_name)

    def log_role_assignment(self, user_id: str, role_name: str) -> None:
        # Logging logic here
        print(f"Role '{role_name}' assigned to user '{user_id}'")

    def log_role_revocation(self, user_id: str, role_name: str) -> None:
        # Logging logic here
        print(f"Role '{role_name}' revoked from user '{user_id}'")