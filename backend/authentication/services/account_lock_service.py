# Epic Title: Implement Account Lockout Mechanism

from datetime import datetime, timedelta
from typing import Tuple
from backend.authentication.models.account_lock_model import db, AccountLock
from backend.authentication.utils import send_email_notification

MAX_FAILED_ATTEMPTS = 5
LOCK_DURATION = timedelta(minutes=15)

class AccountLockService:

    @staticmethod
    def process_login(user_id: int, password: str) -> Tuple[bool, str]:
        account_lock_record = AccountLock.query.filter_by(user_id=user_id).first()

        if account_lock_record:
            if account_lock_record.lock_until and datetime.utcnow() < account_lock_record.lock_until:
                return False, 'Account is locked. Please try again later.'

            if AccountLockService.is_valid_credentials(user_id, password):
                account_lock_record.failed_attempts = 0
                account_lock_record.lock_until = None
                db.session.commit()
                return True, ''
            else:
                account_lock_record.failed_attempts += 1
                if account_lock_record.failed_attempts >= MAX_FAILED_ATTEMPTS:
                    account_lock_record.lock_until = datetime.utcnow() + LOCK_DURATION
                    db.session.commit()
                    send_email_notification(user_id)
                    return False, 'Account is locked due to multiple failed attempts. Check your email for notification.'
                db.session.commit()
                return False, 'Invalid credentials. Please try again.'
        else:
            if AccountLockService.is_valid_credentials(user_id, password):
                new_record = AccountLock(user_id=user_id)
                db.session.add(new_record)
                db.session.commit()
                return True, ''
            else:
                new_record = AccountLock(user_id=user_id, failed_attempts=1)
                db.session.add(new_record)
                db.session.commit()
                return False, 'Invalid credentials. Please try again.'

    @staticmethod
    def is_valid_credentials(user_id: int, password: str) -> bool:
        # This is a placeholder; actual implementation should check credentials securely
        return password == 'correct_password'