# Epic Title: Streamline Service Modification Requests

from flask import Blueprint, request, jsonify
from backend.account_requests.services.service_modification_service import ServiceModificationService

service_modification_controller = Blueprint('service_modification_controller', __name__)

@service_modification_controller.route('/service_modifications', methods=['POST'])
def submit_service_modification_request():
    data = request.get_json()
    user_id = data.get('user_id')
    service_id = data.get('service_id')
    modification_details = data.get('modification_details')

    if not user_id or not service_id or not modification_details:
        return jsonify({'error': 'User ID, Service ID, and Modification Details are required'}), 400

    modification_request = ServiceModificationService.submit_modification_request(user_id, service_id, modification_details)
    return jsonify({
        'message': 'Service modification request submitted successfully',
        'request_id': modification_request.id
    }), 201