# Epic Title: Banking Platform — Core API

from backend.repositories.database.user_request_repository import UserRequestRepository
from backend.models.user_request import UserRequest
from datetime import datetime

class UserRequestService:
    def __init__(self):
        self.repository = UserRequestRepository()

    def log_user_request(self, request_id: str, user_id: str, operation: str):
        timestamp = datetime.now()
        user_request = UserRequest(request_id, user_id, operation, timestamp)
        self.repository.save_user_request(user_request)
        return user_request

    def get_all_user_requests(self) -> list:
        return self.repository.get_user_requests()