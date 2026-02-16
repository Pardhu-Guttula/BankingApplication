# Epic Title: Simplify Account Opening Workflow

from backend.account_requests.repositories.account_opening_repository import AccountOpeningRepository
from backend.account_requests.models.account_opening_request_model import AccountOpeningRequest

class AccountOpeningService:

    @staticmethod
    def submit_account_opening_request(user_id: int, account_type: str) -> dict:
        request: AccountOpeningRequest = AccountOpeningRepository.submit_request(user_id, account_type)
        return {
            'request_id': request.id,
            'status': request.status,
            'submitted_at': request.created_at,
            'message': 'Your account opening request has been submitted successfully.'
        }