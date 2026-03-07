# Epic Title: Banking Platform — Core API

from flask import Blueprint, jsonify, request
from backend.services.notifications.email_service import EmailService

notification_bp = Blueprint('notification_bp', __name__)

@notification_bp.route('/send_email', methods=['POST'])
def send_email():
    data = request.json
    service = EmailService()
    receipt = service.send_email(
        email_id=data['email_id'],
        subject=data['subject'],
        body=data['body'],
        to_email=data['to_email']
    )
    return jsonify({"message": "Email sent successfully", "receipt_id": receipt.receipt_id, "status": receipt.status}), 201