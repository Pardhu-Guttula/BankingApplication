# Epic Title: Streamline Service Modification Requests

from flask import Blueprint, request, jsonify
from backend.account_requests.services.service_modification_service import ServiceModificationService

service_modification_controller = Blueprint('service_modification_controller', __name__)

@service_modification_controller.route('/service/modify', methods=['POST'])
def modify_service():
    data = request.get_json()
    user_id = data.get('user_id')
    modifications = data.get('modifications')
    
    if user_id is None or modifications is None:
        return jsonify({'error': 'Invalid data'}), 400

    success, message = ServiceModificationService.submit_service_modification_request(user_id, modifications)
    if success:
        return jsonify({'message': 'Service modification request submitted successfully'}), 200
    else:
        return jsonify({'error': message}), 400