# Epic Title: Implement Multi-Factor Authentication (MFA)

from backend.authentication.models.otp import OTP
from backend.database import db
from datetime import datetime, timedelta

class OTPRepository:

    def create_otp(self, user_id: int, otp_code: str, method: str) -> OTP:
        new_otp = OTP(
            user_id=user_id,
            otp_code=otp_code,
            method=method,
            expires_at=datetime.utcnow() + timedelta(minutes=5)  # OTP expires in 5 minutes
        )
        db.session.add(new_otp)
        db.session.commit()
        return new_otp

    def get_valid_otp(self, user_id: int, otp_code: str, method: str) -> OTP:
        now = datetime.utcnow()
        return OTP.query.filter(
            OTP.user_id == user_id,
            OTP.otp_code == otp_code,
            OTP.method == method,
            OTP.expires_at > now
        ).first()