# Epic Title: Banking Platform — Core API

from backend.repositories.notifications.notification_repository import NotificationRepository
from backend.models.notifications.update_notification import UpdateNotification
import websocket

class NotificationService:
    def __init__(self):
        self.repository = NotificationRepository()
        self.websocket_url = Settings.WEBSOCKET_URL

    def send_notification(self, request_id: str, status: str, message: str) -> UpdateNotification:
        notification = UpdateNotification(request_id, status, message)
        self.repository.save_notification(notification)
        self._send_via_websocket(notification)
        return notification

    def _send_via_websocket(self, notification: UpdateNotification) -> None:
        ws = websocket.create_connection(self.websocket_url)
        try:
            ws.send(f"{notification.request_id}|{notification.status}|{notification.message}")
        except Exception as e:
            ws.close()
            raise e
        ws.close()