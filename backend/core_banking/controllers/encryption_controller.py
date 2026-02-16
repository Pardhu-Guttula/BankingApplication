# Epic Title: Implement Data Encryption Protocols

from flask import Blueprint, request, jsonify
from backend.core_banking.services.encryption_service import EncryptionService

encryption_controller = Blueprint('encryption_controller', __name__)

@encryption_controller.route('/data/encrypt', methods=['POST'])
def encrypt_data():
    data = request.get_json()
    user_id = data.get('user_id')
    plain_data = data.get('plain_data')
    password = data.get('password')

    if not user_id or not plain_data or not password:
        return jsonify({'error': 'User ID, plain data, and password are required'}), 400

    EncryptionService.encrypt_and_store_data(user_id, plain_data, password)
    return jsonify({'message': 'Data encrypted and stored successfully'}), 200

@encryption_controller.route('/data/decrypt', methods=['POST'])
def decrypt_data():
    data = request.get_json()
    user_id = data.get('user_id')
    record_id = data.get('record_id')
    password = data.get('password')

    if not user_id or not record_id or not password:
        return jsonify({'error': 'User ID, record ID, and password are required'}), 400

    decrypted_data = EncryptionService.retrieve_and_decrypt_data(user_id, record_id, password)
    if decrypted_data:
        return jsonify({'decrypted_data': decrypted_data}), 200
    else:
        return jsonify({'error': 'Invalid credentials or data not found'}), 400