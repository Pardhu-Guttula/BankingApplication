# Epic Title: Implement Account Lockout Mechanism

from datetime import datetime, timedelta
from backend.authentication.models.failed_login_attempt_model import db, FailedLoginAttempt, AccountLockout

class LoginAttemptRepository:

    @staticmethod
    def record_failed_attempt(user_id: int):
        attempt = FailedLoginAttempt(user_id=user_id)
        db.session.add(attempt)
        db.session.commit()

    @staticmethod
    def get_failed_attempts(user_id: int, within_minutes: int) -> int:
        time_threshold = datetime.utcnow() - timedelta(minutes=within_minutes)
        return FailedLoginAttempt.query.filter_by(user_id=user_id).filter(FailedLoginAttempt.timestamp > time_threshold).count()

    @staticmethod
    def lock_account(user_id: int, duration_minutes: int):
        lockout = AccountLockout(user_id=user_id, lockout_duration=duration_minutes)
        db.session.add(lockout)
        db.session.commit()

    @staticmethod
    def is_account_locked(user_id: int) -> bool:
        lockout = AccountLockout.query.filter_by(user_id=user_id).order_by(AccountLockout.lockout_time.desc()).first()
        if lockout:
            lockout_end_time = lockout.lockout_time + timedelta(minutes=lockout.lockout_duration)
            if datetime.utcnow() < lockout_end_time:
                return True
        return False