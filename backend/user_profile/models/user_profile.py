# Epic Title: Update Personal Information

from dataclasses import dataclass
import datetime

@dataclass
class UserProfile:
    user_id: int
    name: str
    email: str
    address: str
    updated_at: datetime.datetime