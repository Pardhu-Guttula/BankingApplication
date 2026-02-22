# Epic Title: Implement user authentication and authorization features

from backend.authentication.models.session import Session

class LogoutService:
    def __init__(self, active_sessions: list[Session]):
        self.active_sessions = active_sessions

    def logout(self, token: str) -> bool:
        for session in self.active_sessions:
            if session.token == token:
                self.active_sessions.remove(session)
                return True
        return False