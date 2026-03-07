# Epic Title: Banking Platform — Core API

from flask import Blueprint, jsonify, request
from backend.services.notifications.email_service import EmailService

notification_bp = Blueprint('notification_bp', __name__)

@notification_bp.route('/send_email', methods=['POST'])
def send_email():
    data = request.json
    service = EmailService()
    receipt = service.send_email(
        template_id=data['template_id'],
        to_email=data['to_email'],
        context=data.get('context', {})
    )
    return jsonify({"message": "Email sent successfully", "receipt_id": receipt.receipt_id, "status": receipt.status}), 201