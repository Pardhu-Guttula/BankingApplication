# Epic Title: Banking Platform — Core API

class User:
    def __init__(self, user_id: str, username: str, password_hash: str):
        self.user_id = user_id
        self.username = username
        self.password_hash = password_hash

class AuthToken:
    def __init__(self, token: str, user_id: str, expires_at: datetime):
        self.token = token
        self.user_id = user_id
        self.expires_at = expires_at