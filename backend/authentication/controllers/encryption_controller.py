# Epic Title: Implement Data Encryption Protocols

from flask import Blueprint, request, jsonify
from backend.authentication.services.encryption_service import EncryptionService

encryption_controller = Blueprint('encryption_controller', __name__)

@encryption_controller.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.get_json()
    plain_text = data.get('plain_text')
    key = data.get('key')

    if plain_text is None or key is None:
        return jsonify({'error': 'Invalid data'}), 400
    
    try:
        encrypted_data = EncryptionService.encrypt_data(plain_text, key.encode())
        return jsonify({'encrypted_data': encrypted_data.hex()}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@encryption_controller.route('/decrypt', methods=['POST'])
def decrypt():
    data = request.get_json()
    cipher_text = bytes.fromhex(data.get('cipher_text'))
    key = data.get('key')

    if cipher_text is None or key is None:
        return jsonify({'error': 'Invalid data'}), 400
    
    try:
        plain_text = EncryptionService.decrypt_data(cipher_text, key.encode())
        return jsonify({'plain_text': plain_text}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500