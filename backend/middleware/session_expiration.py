# Epic Title: Banking Platform — Core API

from backend.services.auth.session_service import SessionService

def session_expiration_middleware(app):
    @app.before_request
    def before_request_func():
        service = SessionService()
        service.remove_expired_tokens()
        service.remove_expired_sessions()