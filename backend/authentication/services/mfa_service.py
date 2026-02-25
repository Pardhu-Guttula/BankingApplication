# Epic Title: Implement Multi-Factor Authentication (MFA)

from backend.authentication.repositories.otp_repository import OTPRepository
from backend.authentication.services.biometric_service import BiometricService
from backend.security.encryption_service import EncryptionService

class MFAService:
    def __init__(self):
        self.otp_repository = OTPRepository()
        self.biometric_service = BiometricService()
        self.encryption_service = EncryptionService()

    def send_otp(self, user_id: int, otp_method: str) -> bool:
        try:
            otp = self.otp_repository.generate_otp(user_id)
            encrypted_otp = self.encryption_service.encrypt(otp.otp_code)
            if otp_method == 'email':
                self._send_email(user_id, encrypted_otp)
            elif otp_method == 'sms':
                self._send_sms(user_id, encrypted_otp)
            return True
        except Exception as e:
            return False

    def verify_otp(self, user_id: int, otp_code: str) -> bool:
        decrypted_otp_code = self.encryption_service.decrypt(otp_code)
        return self.otp_repository.get_valid_otp(user_id, decrypted_otp_code)

    def verify_biometric(self, user_id: int, biometric_data: str) -> bool:
        return self.biometric_service.verify_user_biometric(user_id, biometric_data)

    def _send_email(self, user_id: int, encrypted_otp: str) -> None:
        decrypted_otp = self.encryption_service.decrypt(encrypted_otp)
        # Integrate email sending logic here
        pass

    def _send_sms(self, user_id: int, encrypted_otp: str) -> None:
        decrypted_otp = self.encryption_service.decrypt(encrypted_otp)
        # Integrate SMS sending logic here
        pass
