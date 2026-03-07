# Epic Title: Banking Platform — Core API

class User:
    def __init__(self, user_id: int, username: str, password: str, role: str):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.role = role
        self.last_login = None
        self.created_at = None