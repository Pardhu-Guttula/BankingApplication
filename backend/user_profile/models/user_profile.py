# Epic Title: Change Password

from dataclasses import dataclass

@dataclass
class UserProfile:
    user_id: int
    email: str
    hashed_password: str