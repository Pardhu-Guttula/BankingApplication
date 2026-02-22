# Epic Title: Implement user authentication and authorization features

import datetime
import hashlib
import secrets
from backend.authentication.models.user import User
from backend.authentication.models.session import Session
from backend.authentication.repositories.user_repository import UserRepository

class AuthenticationService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
        self.sessions = []

    def login(self, email: str, password: str) -> Optional[Session]:
        user = self.user_repository.find_by_email(email)
        if not user or user.hashed_password != self.hash_password(password):
            return None
        token = secrets.token_hex(16)
        valid_until = datetime.datetime.now() + datetime.timedelta(hours=12)
        session = Session(secrets.token_hex(8), user.user_id, token, valid_until)
        self.sessions.append(session)
        return session

    def hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()