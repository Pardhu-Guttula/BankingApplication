# Epic Title: Banking Platform — Core API

from flask import request, jsonify
from backend.services.service_modifications.validation_service import ValidationService
from backend.models.service_modifications.modification_request import ModificationRequest

def validate_modification_request(func):
    def wrapper(*args, **kwargs):
        data = request.json
        modification_request = ModificationRequest(
            request_id=data['request_id'],
            user_id=data['user_id'],
            modification_type=data['modification_type'],
            data=data['data']
        )
        validation_result = ValidationService.validate(modification_request)
        if not validation_result.is_valid:
            return jsonify({"message": validation_result.message}), 400
        return func(*args, **kwargs)
    return wrapper