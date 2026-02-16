# Epic Title: Enable Account Opening Requests

from backend.account_management.repositories.account_request_repository import AccountRequestRepository

class AccountRequestService:
    def __init__(self):
        self.account_request_repository = AccountRequestRepository()

    def submit_request(self, user_id: int, account_type: str) -> bool:
        try:
            self.account_request_repository.create_account_request(user_id, account_type)
            return True
        except Exception as e:
            return False