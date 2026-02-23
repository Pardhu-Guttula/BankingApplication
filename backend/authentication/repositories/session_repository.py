# Epic Title: Develop User Logout Capability

from sqlalchemy.orm import Session
from backend.authentication.models.session import Session as UserSession
from typing import Optional

class SessionRepository:
    def __init__(self, db: Session):
        self.db = db

    def invalidate_session_by_token(self, token: str) -> bool:
        session = self.db.query(UserSession).filter(UserSession.token == token).first()
        if session:
            self.db.delete(session)
            self.db.commit()
            return True
        return False

    def get_session_by_token(self, token: str) -> Optional[UserSession]:
        return self.db.query(UserSession).filter(UserSession.token == token).first()