# Epic Title: Manage Account

from sqlalchemy.orm import Session
from backend.account.repositories.account_settings_repository import AccountSettingsRepository

class AccountSettingsService:
    def __init__(self, settings_repository: AccountSettingsRepository):
        self.settings_repository = settings_repository

    def update_account_settings(self, db: Session, user_id: int, email_notifications: bool, sms_notifications: bool, dark_mode: bool, privacy_settings: str):
        settings = self.settings_repository.update_account_settings(user_id, email_notifications, sms_notifications, dark_mode, privacy_settings)
        return settings