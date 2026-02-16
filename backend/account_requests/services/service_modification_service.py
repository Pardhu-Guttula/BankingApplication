# Epic Title: Streamline Service Modification Requests

from backend.account_requests.repositories.service_modification_request_repository import ServiceModificationRequestRepository
from backend.account_requests.services.email_service import EmailService

class ServiceModificationService:

    @staticmethod
    def submit_modification_request(user_id: int, service_id: int, modification_details: str):
        modification_request = ServiceModificationRequestRepository.create_modification_request(user_id, service_id, modification_details)
        EmailService.send_confirmation_email(user_id, modification_request.id)
        return modification_request