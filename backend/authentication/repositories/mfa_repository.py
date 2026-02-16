# Epic Title: Implement Multi-Factor Authentication

from datetime import datetime, timedelta
from backend.authentication.models.mfa_model import db, User, MFAToken

class MFARepository:

    @staticmethod
    def get_user_by_username(username: str) -> User:
        return User.query.filter_by(username=username).first()

    @staticmethod
    def save_mfa_token(user_id: int, token: str, token_type: str, validity_minutes: int) -> MFAToken:
        expires_at = datetime.utcnow() + timedelta(minutes=validity_minutes)
        mfa_token = MFAToken(user_id=user_id, token=token, token_type=token_type, expires_at=expires_at)
        db.session.add(mfa_token)
        db.session.commit()
        return mfa_token

    @staticmethod
    def validate_mfa_token(user_id: int, token: str, token_type: str) -> bool:
        mfa_token = MFAToken.query.filter_by(user_id=user_id, token=token, token_type=token_type).first()
        if mfa_token and mfa_token.expires_at > datetime.utcnow():
            return True
        return False