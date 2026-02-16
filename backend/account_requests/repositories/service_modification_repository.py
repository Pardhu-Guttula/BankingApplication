# Epic Title: Streamline Service Modification Requests

from backend.account_requests.models.service_modification_model import db, ServiceModificationRequest

class ServiceModificationRepository:

    @staticmethod
    def submit_modification_request(user_id: int, service_id: int, modification_type: str) -> ServiceModificationRequest:
        mod_request = ServiceModificationRequest(user_id=user_id, service_id=service_id, modification_type=modification_type)
        db.session.add(mod_request)
        db.session.commit()
        return mod_request