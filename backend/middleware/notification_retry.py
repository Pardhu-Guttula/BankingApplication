# Epic Title: Banking Platform — Core API

from flask import request, jsonify
from backend.services.notifications.notification_service import NotificationService
from backend.models.notifications.update_notification import UpdateNotification
import time

def retry_notification(func):
    def wrapper(*args, **kwargs):
        retries = 3
        data = request.json
        
        for _ in range(retries):
            try:
                notification = NotificationService().send_notification(
                    request_id=data['request_id'],
                    status=data['status'],
                    message=data['message']
                )
                return jsonify({"message": "Notification sent successfully", "request_id": notification.request_id}), 201
            except Exception as e:
                time.sleep(2)
        return jsonify({"message": "Failed to send notification after retries"}), 500
    return wrapper