# Epic Title: Simplify Account Opening Workflow

from backend.account_requests.models.account_opening_request_model import db, AccountOpeningRequest

class AccountOpeningRepository:

    @staticmethod
    def submit_request(user_id: int, account_type: str) -> AccountOpeningRequest:
        request = AccountOpeningRequest(user_id=user_id, account_type=account_type)
        db.session.add(request)
        db.session.commit()
        return request

    @staticmethod
    def get_request_by_id(request_id: int) -> AccountOpeningRequest:
        return AccountOpeningRequest.query.filter_by(id=request_id).first()