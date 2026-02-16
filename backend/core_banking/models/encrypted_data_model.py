# Epic Title: Implement Data Encryption Protocols

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes, kdf
from cryptography.hazmat.backends import default_backend
from base64 import b64encode, b64decode
import os

db = SQLAlchemy()

class EncryptedFinancialData(db.Model):
    __tablename__ = 'encrypted_financial_data'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    encrypted_data = db.Column(db.LargeBinary, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    @staticmethod
    def encrypt_data(data: str, password: str) -> bytes:
        salt = os.urandom(16)
        kdf_instance = kdf.pbkdf2.PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        key = kdf_instance.derive(password.encode())
        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        encrypted = encryptor.update(data.encode()) + encryptor.finalize()
        return b64encode(salt + iv + encrypted)

    @staticmethod
    def decrypt_data(encrypted_data: bytes, password: str) -> str:
        decoded_data = b64decode(encrypted_data)
        salt, iv, encrypted = decoded_data[:16], decoded_data[16:32], decoded_data[32:]
        kdf_instance = kdf.pbkdf2.PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        key = kdf_instance.derive(password.encode())
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        decrypted = decryptor.update(encrypted) + decryptor.finalize()
        return decrypted.decode()