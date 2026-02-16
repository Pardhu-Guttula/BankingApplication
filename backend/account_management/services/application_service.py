# Epic Title: Save and Resume Incomplete Applications

from backend.account_management.repositories.application_repository import ApplicationRepository

class ApplicationService:
    def __init__(self):
        self.application_repository = ApplicationRepository()

    def save_application(self, user_id: int, application_data: dict) -> bool:
        try:
            application_data_json = json.dumps(application_data)
            self.application_repository.save_application(user_id, application_data_json)
            return True
        except Exception:
            return False

    def resume_application(self, user_id: int) -> dict:
        application = self.application_repository.get_application(user_id)
        if application:
            return json.loads(application.application_data)
        return {}