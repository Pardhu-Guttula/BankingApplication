# Epic Title: Streamline Service Modification Requests

from typing import List
from backend.account_requests.models.service_modification_request_model import db, ServiceModificationRequest

class ServiceModificationRequestRepository:

    @staticmethod
    def create_modification_request(user_id: int, service_id: int, modification_details: str) -> ServiceModificationRequest:
        modification_request = ServiceModificationRequest(
            user_id=user_id,
            service_id=service_id,
            modification_details=modification_details,
            status='Pending'
        )
        db.session.add(modification_request)
        db.session.commit()
        return modification_request

    @staticmethod
    def get_user_modification_requests(user_id: int) -> List[ServiceModificationRequest]:
        return ServiceModificationRequest.query.filter_by(user_id=user_id).all()