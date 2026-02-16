# Epic Title: Streamline Service Modification Requests

from backend.account_requests.models.service_modification_request_model import db, ServiceModificationRequest

class ServiceModificationRepository:

    @staticmethod
    def submit_modification_request(user_id: int, service_id: int, modification_details: str) -> ServiceModificationRequest:
        request = ServiceModificationRequest(user_id=user_id, service_id=service_id, modification_details=modification_details)
        db.session.add(request)
        db.session.commit()
        return request

    @staticmethod
    def get_request_by_id(request_id: int) -> ServiceModificationRequest:
        return ServiceModificationRequest.query.filter_by(id=request_id).first()