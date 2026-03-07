# Epic Title: Banking Platform — Core API

from flask import request, jsonify
from backend.services.notifications.email_service import EmailService
import time

def retry_notification(func):
    def wrapper(*args, **kwargs):
        retries = 3
        data = request.json

        for _ in range(retries):
            try:
                receipt = EmailService().send_email(
                    email_id=data['email_id'],
                    subject=data['subject'],
                    body=data['body'],
                    to_email=data['to_email']
                )
                return jsonify({"message": "Email sent successfully", "receipt_id": receipt.receipt_id, "status": receipt.status}), 201
            except Exception as e:
                time.sleep(2)
        return jsonify({"message": "Failed to send email after retries"}), 500
    return wrapper