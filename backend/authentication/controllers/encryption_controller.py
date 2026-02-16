# Epic Title: Implement Data Encryption Protocols

from flask import Blueprint, request, jsonify
from backend.authentication.services.encryption_service import EncryptionService

encryption_controller = Blueprint('encryption_controller', __name__)

@encryption_controller.route('/encrypt', methods=['POST'])
def encrypt_data():
    data = request.json.get('data')
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    encrypted_data = EncryptionService.encrypt(data)
    return jsonify({'encrypted_data': encrypted_data}), 200

@encryption_controller.route('/decrypt', methods=['POST'])
def decrypt_data():
    enc_data = request.json.get('encrypted_data')
    if not enc_data:
        return jsonify({'error': 'No encrypted data provided'}), 400

    decrypted_data = EncryptionService.decrypt(enc_data)
    if not decrypted_data:
        return jsonify({'error': 'Decryption failed'}), 400

    return jsonify({'decrypted_data': decrypted_data}), 200