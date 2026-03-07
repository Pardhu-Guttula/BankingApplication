# Epic Title: Banking Platform — Core API

from backend.repositories.auth.user_repository import UserRepository
from backend.models.auth.user import User, AuthToken
from datetime import datetime, timedelta
import hashlib
import uuid

class AuthenticationService:
    def __init__(self):
        self.user_repository = UserRepository()

    def login(self, username: str, password: str) -> str:
        user = self.user_repository.get_user_by_username(username)
        if user and self.verify_password(password, user.password_hash):
            token = self.generate_token(user)
            return token
        return None

    def verify_password(self, password: str, password_hash: str) -> bool:
        return hashlib.sha256(password.encode()).hexdigest() == password_hash

    def generate_token(self, user: User) -> str:
        token = str(uuid.uuid4())
        expires_at = datetime.now() + timedelta(minutes=30)
        auth_token = AuthToken(token=token, user_id=user.user_id, expires_at=expires_at)
        self.user_repository.save_auth_token(auth_token)
        return token

    def logout(self, token: str) -> None:
        self.user_repository.remove_auth_token(token)

    def validate_token(self, token: str) -> bool:
        auth_token = self.user_repository.get_auth_token(token)
        if auth_token and auth_token.expires_at > datetime.now():
            return True
        return False

    def remove_expired_tokens(self) -> None:
        self.user_repository.remove_expired_tokens()