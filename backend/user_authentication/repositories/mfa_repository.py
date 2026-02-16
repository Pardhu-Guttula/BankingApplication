# Epic Title: Implement Multi-Factor Authentication (MFA)

from datetime import datetime
from backend.user_authentication.models.mfa import MFA
from backend.database import db

class MFARepository:

    def save_otp(self, user_id: int, otp: str, method: str, expires_at: datetime) -> MFA:
        mfa_entry = MFA(user_id=user_id, otp=otp, method=method, expires_at=expires_at)
        db.session.add(mfa_entry)
        db.session.commit()
        return mfa_entry

    def get_valid_otp(self, user_id: int, otp: str) -> MFA:
        return MFA.query.filter_by(user_id=user_id, otp=otp).filter(MFA.expires_at > datetime.utcnow()).first()