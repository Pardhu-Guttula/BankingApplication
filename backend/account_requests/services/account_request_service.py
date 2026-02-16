# Epic Title: Simplify Account Opening Workflow

from backend.account_requests.repositories.account_request_repository import AccountRequestRepository
from backend.account_requests.services.email_service import EmailService

class AccountRequestService:

    @staticmethod
    def submit_account_request(user_id: int):
        account_request = AccountRequestRepository.create_account_request(user_id)
        EmailService.send_confirmation_email(user_id, account_request.id)
        return account_request