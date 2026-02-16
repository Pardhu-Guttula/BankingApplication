# Epic Title: Enable Account Opening Requests

from backend.account_management.repositories.account_opening_repository import AccountOpeningRepository

class AccountOpeningService:
    def __init__(self):
        self.account_opening_repository = AccountOpeningRepository()

    def submit_account_opening_request(self, user_id: int, account_type: str) -> bool:
        try:
            self.account_opening_repository.save_account_opening_request(user_id, account_type)
            return True
        except Exception:
            return False