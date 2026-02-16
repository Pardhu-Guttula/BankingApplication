# Epic Title: Implement Multi-Factor Authentication

import random
import string
from backend.authentication.repositories.mfa_repository import MFARepository
from backend.authentication.models.mfa_model import User

class MFAService:

    @staticmethod
    def generate_token(length: int = 6) -> str:
        return ''.join(random.choices(string.digits, k=length))

    @staticmethod
    def send_mfa_token(user: User, token_type: str) -> str:
        token = MFAService.generate_token()
        MFARepository.save_mfa_token(user.id, token, token_type, validity_minutes=5)

        # Here, you would integrate with an SMS, email, or authenticator app service provider
        if token_type == "sms":
            print(f"Sending SMS token to {user.phone_number}: {token}")
        elif token_type == "email":
            print(f"Sending Email token to {user.email}: {token}")
        elif token_type == "authenticator":
            print(f"Authenticator token generated: {token}")

        return token

    @staticmethod
    def verify_mfa_token(user: User, token: str, token_type: str) -> bool:
        return MFARepository.validate_mfa_token(user.id, token, token_type)