# Epic Title: Streamline Service Modification Requests

from typing import Tuple
from backend.account_requests.models.service_modification_model import db, ServiceModification

class ServiceModificationService:

    @staticmethod
    def submit_service_modification_request(user_id: int, modifications: str) -> Tuple[bool, str]:
        try:
            new_request = ServiceModification(user_id=user_id, modifications=modifications)
            db.session.add(new_request)
            db.session.commit()
            return True, 'Request submitted successfully'
        except Exception as e:
            return False, f'Failed to submit request: {e}'