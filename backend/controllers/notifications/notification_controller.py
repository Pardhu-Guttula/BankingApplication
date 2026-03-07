# Epic Title: Banking Platform — Core API

from flask import Blueprint, jsonify, request
from backend.services.notifications.notification_service import NotificationService

notification_bp = Blueprint('notification_bp', __name__)

@notification_bp.route('/notifications', methods=['GET'])
def get_notifications():
    user_id = request.args.get('user_id')
    service = NotificationService()
    notifications = service.get_notifications(user_id)
    return jsonify([notification.__dict__ for notification in notifications]), 200