# Epic Title: Implement Account Lockout Mechanism

from typing import Tuple
from backend.authentication.repositories.login_attempt_repository import LoginAttemptRepository
from backend.authentication.repositories.locked_account_repository import LockedAccountRepository
from backend.authentication.services.email_service import EmailService

class AccountLockoutService:

    MAX_FAILED_ATTEMPTS = 5
    LOCKOUT_DURATION_MINUTES = 30

    @staticmethod
    def record_attempt_and_check_lockout(user_id: int, success: bool) -> Tuple[bool, str]:
        LoginAttemptRepository.record_login_attempt(user_id, success)
        
        if success:
            return False, 'Login successful'
        
        if LockedAccountRepository.is_account_locked(user_id):
            return True, 'Account is locked'

        recent_attempts = LoginAttemptRepository.get_recent_attempts(user_id)
        failed_attempts = [attempt for attempt in recent_attempts if not attempt.success]
        
        if len(failed_attempts) >= AccountLockoutService.MAX_FAILED_ATTEMPTS:
            LockedAccountRepository.lock_account(user_id, AccountLockoutService.LOCKOUT_DURATION_MINUTES)
            EmailService.send_account_locked_email(user_id)
            return True, 'Account locked due to multiple failed login attempts'

        return False, 'Invalid credentials'