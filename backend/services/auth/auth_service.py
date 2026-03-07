# Epic Title: Banking Platform — Core API

from backend.repositories.auth.user_repository import UserRepository
from backend.repositories.auth.log_repository import LogRepository
from backend.models.auth.user import User
from backend.models.auth.log import Log
import uuid
from datetime import datetime

class AuthService:
    def __init__(self):
        self.user_repository = UserRepository()
        self.log_repository = LogRepository()

    def get_user(self, user_id: str) -> User:
        return self.user_repository.get_user(user_id)

    def perform_authorized_action(self, user_id: str, required_permission: str) -> bool:
        user = self.get_user(user_id)
        # Assume function get_user_roles and get_role_permissions exists
        for role in user.roles:
            permissions = self.role_repository.get_role_permissions(role)
            if required_permission in permissions:
                # Log successful action
                self.log_change(user_id, "authorized_action", f"Action '{required_permission}' performed")
                return True
        # Log unauthorized attempt
        self.log_change(user_id, "unauthorized_action", f"Attempted to perform '{required_permission}'")
        return False

    def log_change(self, user_id: str, action: str, details: str = '') -> None:
        log = Log(
            log_id=str(uuid.uuid4()),
            user_id=user_id,
            action=action,
            timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            details=details
        )
        self.log_repository.save_log(log)

    def get_logs(self, action: str = None) -> list[Log]:
        return self.log_repository.get_logs(action)