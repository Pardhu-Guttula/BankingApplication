# Epic Title: Implement Multi-Factor Authentication

from typing import Optional
from datetime import datetime, timedelta
from backend.authentication.models.mfa_model import db, MFA

class MFARepository:

    @staticmethod
    def create_mfa_record(user_id: int, method: str, code: str, expires_in_minutes: int = 5) -> MFA:
        expires_at = datetime.utcnow() + timedelta(minutes=expires_in_minutes)
        mfa_record = MFA(user_id=user_id, method=method, code=code, expires_at=expires_at)
        db.session.add(mfa_record)
        db.session.commit()
        return mfa_record

    @staticmethod
    def get_mfa_record(user_id: int, code: str) -> Optional[MFA]:
        return MFA.query.filter_by(user_id=user_id, code=code).first()

    @staticmethod
    def delete_mfa_record(mfa_record: MFA) -> None:
        db.session.delete(mfa_record)
        db.session.commit()