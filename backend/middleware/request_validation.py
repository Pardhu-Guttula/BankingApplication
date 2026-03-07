# Epic Title: Banking Platform — Core API

from flask import request, jsonify
from backend.services.account_opening.request_validation_service import RequestValidationService

def validate_request(func):
    def wrapper(*args, **kwargs):
        data = request.json
        request_form = RequestForm(data['user_id'], data['account_type'], data['initial_deposit'])
        if not RequestValidationService.validate(request_form):
            return jsonify({"message": "Invalid request data"}), 400
        return func(*args, **kwargs)
    return wrapper