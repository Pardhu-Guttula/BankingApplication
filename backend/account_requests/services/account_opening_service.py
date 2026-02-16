# Epic Title: Simplify Account Opening Workflow

from typing import Tuple
from backend.account_requests.models.account_request_model import db, AccountRequest

class AccountOpeningService:

    @staticmethod
    def submit_account_opening_request(user_id: int) -> Tuple[bool, str]:
        try:
            new_request = AccountRequest(user_id=user_id)
            db.session.add(new_request)
            db.session.commit()
            return True, 'Request submitted successfully'
        except Exception as e:
            return False, f'Failed to submit request: {e}'