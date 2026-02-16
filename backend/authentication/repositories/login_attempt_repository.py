# Epic Title: Implement Account Lockout Mechanism

from datetime import datetime, timedelta
from typing import List
from backend.authentication.models.login_attempt_model import db, LoginAttempt

class LoginAttemptRepository:

    @staticmethod
    def record_login_attempt(user_id: int, success: bool) -> None:
        attempt = LoginAttempt(user_id=user_id, success=success)
        db.session.add(attempt)
        db.session.commit()

    @staticmethod
    def get_recent_attempts(user_id: int, minutes: int = 30) -> List[LoginAttempt]:
        time_threshold = datetime.utcnow() - timedelta(minutes=minutes)
        return LoginAttempt.query.filter(LoginAttempt.user_id == user_id, LoginAttempt.timestamp >= time_threshold).all()