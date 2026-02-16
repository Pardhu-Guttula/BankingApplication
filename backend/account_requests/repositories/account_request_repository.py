# Epic Title: Simplify Account Opening Workflow

from typing import List
from backend.account_requests.models.account_request_model import db, AccountRequest

class AccountRequestRepository:

    @staticmethod
    def create_account_request(user_id: int) -> AccountRequest:
        account_request = AccountRequest(user_id=user_id, status='Pending')
        db.session.add(account_request)
        db.session.commit()
        return account_request

    @staticmethod
    def get_user_account_requests(user_id: int) -> List[AccountRequest]:
        return AccountRequest.query.filter_by(user_id=user_id).all()