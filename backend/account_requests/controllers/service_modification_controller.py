# Epic Title: Streamline Service Modification Requests

from flask import Blueprint, request, jsonify
from backend.account_requests.services.service_modification_service import ServiceModificationService

service_modification_controller = Blueprint('service_modification_controller', __name__)

@service_modification_controller.route('/service/modify', methods=['POST'])
def modify_service():
    data = request.get_json()
    user_id = data.get('user_id')
    service_id = data.get('service_id')
    modification_details = data.get('modification_details')

    if not user_id or not service_id or not modification_details:
        return jsonify({'error': 'User ID, service ID, and modification details are required'}), 400

    response = ServiceModificationService.submit_service_modification_request(user_id, service_id, modification_details)
    return jsonify(response), 200