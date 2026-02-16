# Epic Title: Integrate Authentication with Bank Security Infrastructure

from backend.authentication.models.auth_integration import AuthIntegration
from backend.database import db

class AuthIntegrationRepository:

    def save_integration_details(self, integration_name: str, integration_details: str) -> AuthIntegration:
        integration = AuthIntegration(integration_name=integration_name, integration_details=integration_details)
        db.session.add(integration)
        db.session.commit()
        return integration

    def get_integration_details(self, integration_name: str) -> AuthIntegration:
        return AuthIntegration.query.filter_by(integration_name=integration_name).first()