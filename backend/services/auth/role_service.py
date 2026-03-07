# Epic Title: Banking Platform — Core API

from backend.repositories.auth.role_repository import RoleRepository
from backend.models.auth.role import Role

class RoleService:
    def __init__(self):
        self.repository = RoleRepository()

    def create_role(self, role_id: str, role_name: str) -> None:
        role = Role(role_id=role_id, role_name=role_name)
        self.repository.create_role(role)

    def update_role(self, role_id: str, role_name: str) -> None:
        role = Role(role_id=role_id, role_name=role_name)
        self.repository.update_role(role)

    def get_role(self, role_id: str) -> Role:
        return self.repository.get_role(role_id)

    def get_all_roles(self) -> list[Role]:
        return self.repository.get_all_roles()