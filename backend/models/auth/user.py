# Epic Title: Banking Platform — Core API

class User:
    def __init__(self, user_id: str, username: str, roles: list[str] = None):
        self.user_id = user_id
        self.username = username
        self.roles = roles if roles else []