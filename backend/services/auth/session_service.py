# Epic Title: Banking Platform — Core API

from backend.repositories.auth.session_repository import SessionRepository
from backend.models.auth.user_session import UserSession, AuthToken
from datetime import datetime, timedelta
import hashlib
import uuid

class SessionService:
    def __init__(self):
        self.repository = SessionRepository()

    def create_session(self, user_id: str) -> str:
        session_id = str(uuid.uuid4())
        expires_at = datetime.now() + timedelta(minutes=30)
        user_session = UserSession(session_id, user_id, expires_at)
        self.repository.save_user_session(user_session)
        return session_id

    def get_session(self, session_id: str) -> UserSession:
        return self.repository.get_user_session(session_id)

    def create_auth_token(self, user_id: str) -> str:
        token = str(uuid.uuid4())
        expires_at = datetime.now() + timedelta(minutes=30)
        auth_token = AuthToken(token, user_id, expires_at)
        self.repository.save_auth_token(auth_token)
        return token

    def validate_auth_token(self, token: str) -> bool:
        auth_token = self.repository.get_auth_token(token)
        if auth_token and auth_token.expires_at > datetime.now():
            return True
        return False

    def invalidate_auth_token(self, token: str):
        self.repository.remove_auth_token(token)

    def remove_expired_tokens(self):
        self.repository.remove_expired_tokens()

    def remove_expired_sessions(self):
        self.repository.remove_expired_sessions()