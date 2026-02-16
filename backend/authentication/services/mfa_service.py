# Epic Title: Implement Multi-Factor Authentication (MFA)

from backend.authentication.repositories.otp_repository import OTPRepository
from backend.authentication.services.biometric_service import BiometricService

class MFAService:
    def __init__(self):
        self.otp_repository = OTPRepository()
        self.biometric_service = BiometricService()

    def send_otp(self, user_id: int, otp_method: str) -> bool:
        try:
            otp = self.otp_repository.generate_otp(user_id)
            if otp_method == 'email':
                self._send_email(user_id, otp.otp_code)
            elif otp_method == 'sms':
                self._send_sms(user_id, otp.otp_code)
            return True
        except Exception as e:
            return False

    def verify_otp(self, user_id: int, otp_code: str) -> bool:
        return self.otp_repository.get_valid_otp(user_id, otp_code)

    def verify_biometric(self, user_id: int, biometric_data: str) -> bool:
        return self.biometric_service.verify_user_biometric(user_id, biometric_data)

    def _send_email(self, user_id: int, otp_code: str) -> None:
        # Integrate email sending logic here
        pass

    def _send_sms(self, user_id: int, otp_code: str) -> None:
        # Integrate SMS sending logic here
        pass