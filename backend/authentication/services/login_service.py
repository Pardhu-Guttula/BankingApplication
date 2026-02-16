# Epic Title: Implement Account Lockout Mechanism

from werkzeug.security import check_password_hash
from backend.authentication.repositories.login_attempt_repository import LoginAttemptRepository
from backend.authentication.models.login_attempt_model import User

class LoginService:

    @staticmethod
    def authenticate_user(username: str, password: str) -> bool:
        user = User.query.filter_by(username=username).first()
        if user and not LoginAttemptRepository.is_account_locked(user.id):
            if check_password_hash(user.password, password):
                LoginAttemptRepository.reset_failed_attempts(user.id)
                return True
            else:
                LoginAttemptRepository.record_login_attempt(user.id, successful=False)
        elif user:
            LoginAttemptRepository.record_login_attempt(user.id, successful=False)        
        return False