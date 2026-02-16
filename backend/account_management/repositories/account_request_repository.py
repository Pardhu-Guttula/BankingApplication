# Epic Title: Enable Account Opening Requests

from backend.account_management.models.account_request import AccountRequest
from backend.database import db

class AccountRequestRepository:

    def create_account_request(self, user_id: int, account_type: str) -> AccountRequest:
        new_request = AccountRequest(
            user_id=user_id,
            account_type=account_type
        )
        db.session.add(new_request)
        db.session.commit()
        return new_request