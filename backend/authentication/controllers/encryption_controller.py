# Epic Title: Implement Data Encryption Protocols

from flask import Blueprint, request, jsonify
from backend.authentication.services.encryption_service import EncryptionService

encryption_controller = Blueprint('encryption_controller', __name__)

@encryption_controller.route('/encrypt', methods=['POST'])
def encrypt_data():
    data = request.get_json()
    plain_text = data.get('plain_text')

    if plain_text is None:
        return jsonify({'error': 'Invalid data'}), 400

    encrypted_text, error = EncryptionService.encrypt_data(plain_text)
    if error:
        return jsonify({'error': error}), 500
        
    return jsonify({'encrypted_text': encrypted_text}), 200

@encryption_controller.route('/decrypt', methods=['POST'])
def decrypt_data():
    data = request.get_json()
    encrypted_text = data.get('encrypted_text')

    if encrypted_text is None:
        return jsonify({'error': 'Invalid data'}), 400

    plain_text, error = EncryptionService.decrypt_data(encrypted_text)
    if error:
        return jsonify({'error': error}), 500
        
    return jsonify({'plain_text': plain_text}), 200