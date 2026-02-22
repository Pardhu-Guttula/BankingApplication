# Epic Title: Implement user authentication and authorization features

from typing import List

class Role:
    def __init__(self, role_id: int, name: str, permissions: List[str]):
        self.role_id = role_id
        self.name = name
        self.permissions = permissions