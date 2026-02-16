# Epic Title: Implement Multi-Factor Authentication

import random
import string
from typing import Tuple
from backend.authentication.models.mfa_model import db, MFA
from backend.authentication.utils import send_sms, send_email, send_app_notification

class MFAService:

    @staticmethod
    def generate_code() -> str:
        return ''.join(random.choices(string.digits, k=6))

    @staticmethod
    def send_code(user_id: int, method: str) -> Tuple[bool, str]:
        code = MFAService.generate_code()
        mfa_record = MFA.query.filter_by(user_id=user_id).first()
        
        if mfa_record:
            mfa_record.mfa_code = code
            mfa_record.method = method
            mfa_record.created_at = datetime.utcnow()
            mfa_record.expires_at = datetime.utcnow() + timedelta(minutes=5)
        else:
            mfa_record = MFA(
                user_id=user_id,
                mfa_code=code,
                method=method
            )
            db.session.add(mfa_record)

        db.session.commit()

        if method == 'SMS':
            return send_sms(user_id, code)
        elif method == 'Email':
            return send_email(user_id, code)
        elif method == 'App':
            return send_app_notification(user_id, code)
        else:
            return False, 'Invalid MFA method'

    @staticmethod
    def verify_code(user_id: int, code: str) -> Tuple[bool, str]:
        mfa_record = MFA.query.filter_by(user_id=user_id, mfa_code=code).first()
        if mfa_record and not mfa_record.is_expired():
            return True, ''
        return False, 'Invalid or expired MFA code'