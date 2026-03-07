# Epic Title: Banking Platform — Core API

from backend.repositories.account_opening.account_repository import AccountRepository
from backend.models.account_opening.account import Account
import uuid

class AccountService:
    def __init__(self):
        self.repository = AccountRepository()

    def create_account(self, user_id: str, account_type: str, initial_deposit: float) -> Account:
        account_id = str(uuid.uuid4())
        account = Account(account_id, user_id, account_type, initial_deposit)
        self.repository.save_account(account)
        return account