# Epic Title: Banking Platform — Core API

from datetime import datetime

class UserRequest:
    def __init__(self, request_id: str, user_id: str, operation: str, timestamp: datetime):
        self.request_id = request_id
        self.user_id = user_id
        self.operation = operation
        self.timestamp = timestamp