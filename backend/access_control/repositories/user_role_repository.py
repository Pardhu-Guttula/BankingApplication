# Epic Title: Implement Role-Based Access Control

from sqlalchemy.orm import Session
from backend.access_control.models.user_role import UserRole
from typing import Optional

class UserRoleRepository:
    def __init__(self, db: Session):
        self.db = db

    def assign_role_to_user(self, user_id: int, role_id: int) -> UserRole:
        user_role = UserRole(user_id=user_id, role_id=role_id)
        self.db.add(user_role)
        self.db.commit()
        self.db.refresh(user_role)
        return user_role

    def get_user_role(self, user_id: int) -> Optional[UserRole]:
        return self.db.query(UserRole).filter(UserRole.user_id == user_id).first()

    def change_user_role(self, user_id: int, new_role_id: int) -> UserRole:
        user_role = self.get_user_role(user_id)
        if user_role:
            user_role.role_id = new_role_id
            self.db.commit()
            self.db.refresh(user_role)
        return user_role