# Epic Title: Streamline Service Modification Requests

from backend.account_requests.repositories.service_modification_repository import ServiceModificationRepository
from backend.account_requests.models.service_modification_model import ServiceModificationRequest

class ServiceModificationService:

    @staticmethod
    def create_modification_request(user_id: int, service_id: int, modification_type: str) -> ServiceModificationRequest:
        return ServiceModificationRepository.submit_modification_request(user_id, service_id, modification_type)