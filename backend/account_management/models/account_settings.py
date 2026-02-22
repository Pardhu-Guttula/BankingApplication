# Epic Title: Manage Account

from dataclasses import dataclass
import datetime

@dataclass
class AccountSettings:
    user_id: int
    preferences: str
    privacy_settings: str
    updated_at: datetime.datetime