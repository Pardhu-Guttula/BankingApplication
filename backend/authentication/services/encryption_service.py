# Epic Title: Implement Data Encryption Protocols

import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding, hashes
from typing import Tuple
from backend.authentication.models.encryption_keys_model import db, EncryptionKey

class EncryptionService:

    @staticmethod
    def generate_key(user_id: int) -> str:
        key = base64.urlsafe_b64encode(os.urandom(32)).decode('utf-8')
        encryption_key = EncryptionKey(user_id=user_id, key=key)
        db.session.add(encryption_key)
        db.session.commit()
        return key

    @staticmethod
    def get_key(user_id: int) -> EncryptionKey:
        return EncryptionKey.query.filter_by(user_id=user_id).first()

    @staticmethod
    def encrypt_data(plain_text: str) -> Tuple[str, str]:
        try:
            # Example user_id, in practice this should be fetched from an authenticated session
            user_id = 1  
            key_record = EncryptionService.get_key(user_id)
            if not key_record:
                key = EncryptionService.generate_key(user_id)
            else:
                key = key_record.key.encode('utf-8')

            # Encrypt
            plain_text_bytes = plain_text.encode('utf-8')
            iv = os.urandom(16)
            cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
            encryptor = cipher.encryptor()
            padded_data = padder.update(plain_text_bytes) + padder.finalize()
            encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
            encrypted_text = base64.b64encode(iv + encrypted_data).decode('utf-8')
            return encrypted_text, ''
        except Exception as e:
            return '', str(e)

    @staticmethod
    def decrypt_data(encrypted_text: str) -> Tuple[str, str]:
        try:
            user_id = 1
            key_record = EncryptionService.get_key(user_id)
            if not key_record:
                return '', 'Encryption key not found'
            key = key_record.key.encode('utf-8')

            encrypted_data_bytes = base64.b64decode(encrypted_text.encode('utf-8'))
            iv = encrypted_data_bytes[:16]
            encrypted_data = encrypted_data_bytes[16:]
            cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
            decryptor = cipher.decryptor()
            padded_data = decryptor.update(encrypted_data) + decryptor.finalize()
            unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
            plain_text_bytes = unpadder.update(padded_data) + unpadder.finalize()
            plain_text = plain_text_bytes.decode('utf-8')
            return plain_text, ''
        except Exception as e:
            return '', str(e)