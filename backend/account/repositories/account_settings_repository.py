# Epic Title: Manage Account

from sqlalchemy.orm import Session
from backend.account.models.account_settings import AccountSettings

class AccountSettingsRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_settings_by_user_id(self, user_id: int) -> AccountSettings:
        return self.db.query(AccountSettings).filter(AccountSettings.user_id == user_id).first()

    def update_account_settings(self, user_id: int, email_notifications: bool, sms_notifications: bool, dark_mode: bool, privacy_settings: str) -> AccountSettings:
        settings = self.get_settings_by_user_id(user_id)
        if settings:
            settings.email_notifications = email_notifications
            settings.sms_notifications = sms_notifications
            settings.dark_mode = dark_mode
            settings.privacy_settings = privacy_settings
            self.db.commit()
            self.db.refresh(settings)
        return settings