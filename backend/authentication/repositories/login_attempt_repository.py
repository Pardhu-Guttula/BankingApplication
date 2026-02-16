# Epic Title: Implement Account Lockout Mechanism

from datetime import datetime, timedelta
from backend.authentication.models.login_attempt_model import db, User, LoginAttempt

class LoginAttemptRepository:

    @staticmethod
    def record_login_attempt(user_id: int, successful: bool):
        attempt = LoginAttempt(user_id=user_id, successful=successful)
        db.session.add(attempt)
        db.session.commit()

        if not successful:
            user = User.query.filter_by(id=user_id).first()
            user.failed_login_attempts += 1
            if user.failed_login_attempts >= 5:
                user.is_locked = True
                user.lockout_until = datetime.utcnow() + timedelta(minutes=30)  # lockout for 30 minutes
                # Send email notification here
                print(f"Sending lockout email to {user.email}")
            db.session.commit()

    @staticmethod
    def reset_failed_attempts(user_id: int):
        user = User.query.filter_by(id=user_id).first()
        user.failed_login_attempts = 0
        user.is_locked = False
        user.lockout_until = None
        db.session.commit()

    @staticmethod
    def is_account_locked(user_id: int) -> bool:
        user = User.query.filter_by(id=user_id).first()
        if user.is_locked and user.lockout_until > datetime.utcnow():
            return True
        return False