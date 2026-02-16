# Epic Title: Implement Account Lockout Mechanism

from datetime import datetime
from typing import Optional
from backend.authentication.models.locked_account_model import db, LockedAccount

class LockedAccountRepository:

    @staticmethod
    def lock_account(user_id: int, lock_duration_minutes: int) -> None:
        locked_until = datetime.utcnow() + timedelta(minutes=lock_duration_minutes)
        locked_account = LockedAccount(user_id=user_id, locked_until=locked_until)
        db.session.merge(locked_account)
        db.session.commit()

    @staticmethod
    def is_account_locked(user_id: int) -> bool:
        locked_account: Optional[LockedAccount] = LockedAccount.query.filter_by(user_id=user_id).first()
        if locked_account and locked_account.locked_until > datetime.utcnow():
            return True
        return False

    @staticmethod
    def unlock_account(user_id: int) -> None:
        LockedAccount.query.filter_by(user_id=user_id).delete()
        db.session.commit()