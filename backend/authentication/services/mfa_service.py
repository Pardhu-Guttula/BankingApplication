# Epic Title: Implement Multi-Factor Authentication (MFA)

import logging
import random
from backend.authentication.repositories.otp_repository import OTPRepository

class MFAService:
    def __init__(self):
        self.otp_repository = OTPRepository()

    def generate_otp(self, user_id: int, method: str) -> None:
        otp_code = self._generate_random_otp()
        self.otp_repository.create_otp(user_id, otp_code, method)
        self._send_otp(user_id, otp_code, method)

    def _generate_random_otp(self) -> str:
        return ''.join([str(random.randint(0, 9)) for _ in range(6)])

    def _send_otp(self, user_id: int, otp_code: str, method: str) -> None:
        # Placeholder for actual sending logic (email, SMS, biometric)
        logging.info(f'Sending OTP {otp_code} to user {user_id} via {method}')