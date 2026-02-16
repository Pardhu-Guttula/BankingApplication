# Epic Title: Implement Account Lockout Mechanism

from backend.authentication.repositories.login_attempt_repository import LoginAttemptRepository
from backend.authentication.services.email_service import EmailService

class LoginService:

    MAX_FAILED_ATTEMPTS = 5
    LOCKOUT_DURATION_MINUTES = 30

    @staticmethod
    def handle_failed_login(user_id: int):
        if LoginAttemptRepository.is_account_locked(user_id):
            raise Exception("Account is locked")

        LoginAttemptRepository.record_failed_attempt(user_id)
        failed_attempts = LoginAttemptRepository.get_failed_attempts(user_id, LoginService.LOCKOUT_DURATION_MINUTES)

        if failed_attempts >= LoginService.MAX_FAILED_ATTEMPTS:
            LoginAttemptRepository.lock_account(user_id, LoginService.LOCKOUT_DURATION_MINUTES)
            EmailService.send_account_lockout_notification(user_id)