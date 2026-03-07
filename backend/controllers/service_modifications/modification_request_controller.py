# Epic Title: Banking Platform — Core API

from flask import Blueprint, jsonify, request
from backend.services.service_modifications.validation_service import ValidationService
from backend.services.service_modifications.process_service import ProcessService
from backend.repositories.service_modifications.modification_request_repository import ModificationRequestRepository
from backend.models.service_modifications.modification_request import ModificationRequest
from backend.models.service_modifications.process_result import ProcessResult

modification_request_bp = Blueprint('modification_request_bp', __name__)

@modification_request_bp.route('/process_modification_request', methods=['POST'])
def process_modification_request():
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

    process_result = ProcessService.process(modification_request)
    return jsonify({"message": process_result.message}), 200 if process_result.success else 500