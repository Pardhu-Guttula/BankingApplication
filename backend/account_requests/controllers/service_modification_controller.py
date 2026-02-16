# Epic Title: Streamline Service Modification Requests

from flask import Blueprint, request, jsonify
from backend.account_requests.services.service_modification_service import ServiceModificationService

service_modification_controller = Blueprint('service_modification_controller', __name__)

@service_modification_controller.route('/service/modify', methods=['POST'])
def modify_service():
    data = request.get_json()
    user_id = data.get('user_id')
    service_id = data.get('service_id')
    modification_type = data.get('modification_type')

    if not user_id or not service_id or not modification_type:
        return jsonify({'error': 'User ID, service ID and modification type are required'}), 400

    mod_request = ServiceModificationService.create_modification_request(user_id, service_id, modification_type)
    return jsonify({
        'message': 'Service modification request submitted successfully',
        'request_id': mod_request.id,
        'status': mod_request.status
    }), 200