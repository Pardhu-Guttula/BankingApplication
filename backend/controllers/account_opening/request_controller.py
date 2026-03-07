# Epic Title: Banking Platform — Core API

from flask import Blueprint, jsonify, request
from backend.services.account_opening.request_validation_service import RequestValidationService
from backend.repositories.account_opening.request_form_repository import RequestFormRepository
from backend.models.account_opening.request_form import RequestForm

request_bp = Blueprint('request_bp', __name__)

@request_bp.route('/submit_request', methods=['POST'])
def submit_request():
    data = request.json
    request_form = RequestForm(data['user_id'], data['account_type'], data['initial_deposit'])
    
    if not RequestValidationService.validate(request_form):
        return jsonify({"message": "Invalid request data"}), 400
    
    repository = RequestFormRepository()
    repository.save_request_form(request_form)
    return jsonify({"message": "Request submitted successfully"}), 201