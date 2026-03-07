# Epic Title: Banking Platform — Core API

from flask import Blueprint, jsonify, request
from backend.services.notifications.notification_service import NotificationService

notification_bp = Blueprint('notification_bp', __name__)

@notification_bp.route('/send_notification', methods=['POST'])
def send_notification():
    data = request.json
    service = NotificationService()
    notification = service.send_notification(
        request_id=data['request_id'],
        status=data['status'],
        message=data['message']
    )
    return jsonify({"message": "Notification sent successfully", "request_id": notification.request_id}), 201