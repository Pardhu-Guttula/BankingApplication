# Epic Title: Implement user authentication and authorization features

from typing import Optional
import datetime

class Session:
    def __init__(self, session_id: str, user_id: int, token: str, valid_until: datetime.datetime):
        self.session_id = session_id
        self.user_id = user_id
        self.token = token
        self.valid_until = valid_until

    def is_valid(self) -> bool:
        return datetime.datetime.now() < self.valid_until