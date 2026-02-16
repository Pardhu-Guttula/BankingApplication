# Epic Title: Simplify Account Opening Workflow

from backend.account_requests.models.account_request_model import db, AccountRequest

class AccountRequestRepository:

    @staticmethod
    def submit_account_request(user_id: int, request_type: str) -> AccountRequest:
        account_request = AccountRequest(user_id=user_id, request_type=request_type)
        db.session.add(account_request)
        db.session.commit()
        return account_request