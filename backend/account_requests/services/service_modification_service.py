# Epic Title: Streamline Service Modification Requests

from backend.account_requests.repositories.service_modification_repository import ServiceModificationRepository
from backend.account_requests.models.service_modification_request_model import ServiceModificationRequest

class ServiceModificationService:

    @staticmethod
    def submit_service_modification_request(user_id: int, service_id: int, modification_details: str) -> dict:
        request: ServiceModificationRequest = ServiceModificationRepository.submit_modification_request(user_id, service_id, modification_details)
        return {
            'request_id': request.id,
            'status': request.status,
            'submitted_at': request.created_at,
            'message': 'Your service modification request has been submitted successfully.'
        }