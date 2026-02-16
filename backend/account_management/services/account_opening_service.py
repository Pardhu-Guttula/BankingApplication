# Epic Title: Enable Account Opening Requests

from backend.account_management.repositories.account_request_repository import AccountRequestRepository

class AccountOpeningService:
    def __init__(self):
        self.account_request_repository = AccountRequestRepository()

    def submit_account_request(self, user_id: int, account_type: str, initial_deposit: float) -> bool:
        try:
            self.account_request_repository.submit_request(user_id, account_type, initial_deposit)
            return True
        except Exception as e:
            return False