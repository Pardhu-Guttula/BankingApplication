# Epic Title: Develop User Logout Capability

from sqlalchemy.orm import Session
from werkzeug.security import check_password_hash
from datetime import datetime, timedelta
import jwt

from backend.authentication.repositories.user_repository import UserRepository
from backend.authentication.repositories.session_repository import SessionRepository
from backend.authentication.models.user import User
from backend.authentication.models.session import Session

class LoginService:
    def __init__(self, user_repository: UserRepository, session_repository: SessionRepository):
        self.user_repository = user_repository
        self.session_repository = session_repository

    def authenticate_user(self, db: Session, email: str, password: str) -> Optional[str]:
        user = self.user_repository.get_user_by_email(email)
        if user and check_password_hash(user.password_hash, password):
            token = jwt.encode({'user_id': user.id, 'exp': datetime.utcnow() + timedelta(hours=1)}, 'secret', algorithm='HS256')
            session = self.session_repository.create_session(user.id, token, datetime.utcnow() + timedelta(hours=1))
            return token
        else:
            return None