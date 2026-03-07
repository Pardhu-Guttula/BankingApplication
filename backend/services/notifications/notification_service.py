# Epic Title: Banking Platform — Core API

from backend.repositories.notifications.notification_repository import NotificationRepository
from backend.models.notifications.notification import Notification
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
from backend.config.settings import Settings

class NotificationService:
    def __init__(self):
        self.repository = NotificationRepository()

    def send_notification(self, user_id: str, notification_type: str, message: str) -> None:
        notification = Notification(
            user_id=user_id,
            notification_type=notification_type,
            message=message,
            timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        )
        self.repository.save_notification(notification)
        msg = MIMEText(message)
        msg["Subject"] = f"{notification_type} Notification"
        msg["From"] = "noreply@example.com"
        msg["To"] = Settings.ADMIN_EMAIL

        with smtplib.SMTP(Settings.SMTP_SERVER, Settings.SMTP_PORT) as server:
            server.sendmail("noreply@example.com", [Settings.ADMIN_EMAIL], msg.as_string())

    def get_notifications(self, user_id: str) -> list[Notification]:
        return self.repository.get_notifications(user_id)