# Epic Title: Banking Platform — Core API

from flask import Blueprint, jsonify, request
from backend.services.service_modifications.validation_service import ValidationService
from backend.repositories.service_modifications.modification_request_repository import ModificationRequestRepository
from backend.models.service_modifications.modification_request import ModificationRequest

modification_request_bp = Blueprint('modification_request_bp', __name__)

@modification_request_bp.route('/validate_modification_request', methods=['POST'])
def validate_modification_request():
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
    
    repository = ModificationRequestRepository()
    repository.save_modification_request(modification_request)
    return jsonify({"message": "Modification request is valid and has been saved"}), 200