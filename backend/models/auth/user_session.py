# Epic Title: Banking Platform — Core API

from datetime import datetime

class UserSession:
    def __init__(self, session_id: str, user_id: str, expires_at: datetime):
        self.session_id = session_id
        self.user_id = user_id
        self.expires_at = expires_at

class AuthToken:
    def __init__(self, token: str, user_id: str, expires_at: datetime):
        self.token = token
        self.user_id = user_id
        self.expires_at = expires_at