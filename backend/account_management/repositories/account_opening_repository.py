# Epic Title: Enable Account Opening Requests

from backend.account_management.models.account_opening import AccountOpeningRequest
from backend.database import db

class AccountOpeningRepository:

    def save_account_opening_request(self, user_id: int, account_type: str) -> AccountOpeningRequest:
        request = AccountOpeningRequest(user_id=user_id, account_type=account_type)
        db.session.add(request)
        db.session.commit()
        return request