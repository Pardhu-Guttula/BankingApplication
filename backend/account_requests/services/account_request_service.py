# Epic Title: Simplify Account Opening Workflow

from backend.account_requests.repositories.account_request_repository import AccountRequestRepository
from backend.account_requests.models.account_request_model import AccountRequest

class AccountRequestService:

    @staticmethod
    def create_account_request(user_id: int, request_type: str) -> AccountRequest:
        return AccountRequestRepository.submit_account_request(user_id, request_type)