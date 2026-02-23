# Epic Title: Develop User Login Capability

from sqlalchemy.orm import Session
from backend.authentication.models.session import Session as UserSession
from typing import Optional

class SessionRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_session(self, user_id: int, token: str, expires_at: str) -> UserSession:
        db_session = UserSession(user_id=user_id, token=token, created_at=datetime.utcnow(), expires_at=expires_at)
        self.db.add(db_session)
        self.db.commit()
        self.db.refresh(db_session)
        return db_session

    def get_session_by_token(self, token: str) -> Optional[UserSession]:
        return self.db.query(UserSession).filter(UserSession.token == token).first()