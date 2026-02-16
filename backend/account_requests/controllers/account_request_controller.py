# Epic Title: Simplify Account Opening Workflow

from flask import Blueprint, request, jsonify
from backend.account_requests.services.account_request_service import AccountRequestService

account_request_controller = Blueprint('account_request_controller', __name__)

@account_request_controller.route('/account/request', methods=['POST'])
def create_account_request():
    data = request.get_json()
    user_id = data.get('user_id')
    request_type = data.get('request_type')

    if not user_id or not request_type:
        return jsonify({'error': 'User ID and request type are required'}), 400

    account_request = AccountRequestService.create_account_request(user_id, request_type)
    return jsonify({
        'message': 'Account request submitted successfully',
        'request_id': account_request.id,
        'status': account_request.status
    }), 200

@account_request_controller.route('/account/request/documents', methods=['POST'])
def upload_account_request_documents():
    data = request.get_json()
    user_id = data.get('user_id')
    document = data.get('document')

    if not user_id or not document:
        return jsonify({'error': 'User ID and document are required'}), 400

    AccountRequestService.upload_document(user_id, document)
    return jsonify({
        'message': 'Document uploaded successfully'
    }), 200
