# Epic Title: Save and Resume Incomplete Applications

from backend.account_management.models.application import Application
from backend.database import db

class ApplicationRepository:

    def save_application(self, user_id: int, application_data: str) -> Application:
        existing_application = Application.query.filter_by(user_id=user_id).first()
        if existing_application:
            existing_application.application_data = application_data
            db.session.commit()
            return existing_application
        new_application = Application(user_id=user_id, application_data=application_data)
        db.session.add(new_application)
        db.session.commit()
        return new_application

    def get_application(self, user_id: int) -> Application:
        return Application.query.filter_by(user_id=user_id).first()