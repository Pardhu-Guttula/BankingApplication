# Epic Title: Save and Resume Incomplete Applications

from backend.account_management.repositories.application_repository import ApplicationRepository

class ApplicationService:
    def __init__(self):
        self.application_repository = ApplicationRepository()

    def save_application(self, user_id: int, application_data: str) -> bool:
        try:
            self.application_repository.save_application(user_id, application_data)
            return True
        except Exception as e:
            return False

    def get_saved_application(self, user_id: int) -> dict:
        application = self.application_repository.get_application_by_user(user_id)
        if application:
            return {
                "application_data": application.application_data,
                "status": application.status
            }
        return None