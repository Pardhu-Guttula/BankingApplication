# Epic Title: Implement user authentication and authorization features

class User:
    def __init__(self, user_id: int, name: str, email: str, role_id: int):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.role_id = role_id