# Epic Title: Enable Account Opening Requests

from backend.account_management.models.account_request import AccountRequest
from backend.database import db

class AccountRequestRepository:

    def submit_request(self, user_id: int, account_type: str, initial_deposit: float) -> AccountRequest:
        account_request = AccountRequest(
            user_id=user_id,
            account_type=account_type,
            initial_deposit=initial_deposit
        )
        db.session.add(account_request)
        db.session.commit()
        return account_request