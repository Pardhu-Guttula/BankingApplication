# Epic Title: Implement user authentication and authorization features

from typing import List, Optional
from backend.access_control.models.role import Role

class RoleRepository:
    def __init__(self):
        self.roles = [
            Role(1, "admin", ["manage_users", "view_reports", "edit_content"]),
            Role(2, "user", ["view_content", "comment"]),
            Role(3, "guest", ["view_content"])
        ]

    def get_role_by_name(self, name: str) -> Optional[Role]:
        for role in self.roles:
            if role.name == name:
                return role
        return None