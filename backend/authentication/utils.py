# Epic Title: Implement Multi-Factor Authentication

from typing import Tuple

def send_sms(user_id: int, code: str) -> Tuple[bool, str]:
    # Dummy SMS sending logic
    print(f"Sending SMS to user {user_id} with code: {code}")
    return True, ''

def send_email(user_id: int, code: str) -> Tuple[bool, str]:
    # Dummy Email sending logic
    print(f"Sending Email to user {user_id} with code: {code}")
    return True, ''

def send_app_notification(user_id: int, code: str) -> Tuple[bool, str]:
    # Dummy App Notification sending logic
    print(f"Sending App Notification to user {user_id} with code: {code}")
    return True, ''