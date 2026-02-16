# Epic Title: Implement Multi-Factor Authentication

from backend.authentication.models.mfa_model import db, MFA

class MFARepository:

    @staticmethod
    def create_mfa(user_id: int, mfa_type: str, mfa_secret: str) -> MFA:
        mfa = MFA(user_id=user_id, mfa_type=mfa_type, mfa_secret=mfa_secret)
        db.session.add(mfa)
        db.session.commit()
        return mfa

    @staticmethod
    def get_active_mfa(user_id: int) -> MFA:
        return MFA.query.filter_by(user_id=user_id, is_active=True).first()

    @staticmethod
    def deactivate_mfa(user_id: int):
        mfa = MFA.query.filter_by(user_id=user_id, is_active=True).first()
        if mfa:
            mfa.is_active = False
            db.session.commit()