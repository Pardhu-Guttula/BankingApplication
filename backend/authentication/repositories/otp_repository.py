# Epic Title: Implement Multi-Factor Authentication (MFA)

from datetime import datetime, timedelta
from backend.authentication.models.otp import OTP
from backend.database import db
import random

class OTPRepository:

    def generate_otp(self, user_id: int) -> OTP:
        otp_code = f"{random.randint(100000, 999999)}"
        expires_at = datetime.utcnow() + timedelta(minutes=5)
        otp = OTP(user_id=user_id, otp_code=otp_code, expires_at=expires_at)
        db.session.add(otp)
        db.session.commit()
        return otp

    def get_valid_otp(self, user_id: int, otp_code: str) -> bool:
        otp = OTP.query.filter_by(user_id=user_id, otp_code=otp_code).first()
        if otp and otp.expires_at > datetime.utcnow():
            return True
        return False