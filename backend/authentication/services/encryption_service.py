# Epic Title: Implement Data Encryption Protocols

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

class EncryptionService:

    @staticmethod
    def encrypt_data(plain_text: str, key: bytes) -> bytes:
        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(plain_text.encode()) + padder.finalize()
        encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
        return iv + encrypted_data

    @staticmethod
    def decrypt_data(cipher_text: bytes, key: bytes) -> str:
        iv = cipher_text[:16]
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        padded_data = decryptor.update(cipher_text[16:]) + decryptor.finalize()
        unpadder = padding.PKCS7(128).unpadder()
        plain_text = unpadder.update(padded_data) + unpadder.finalize()
        return plain_text.decode()

    @staticmethod
    def generate_key() -> bytes:
        return os.urandom(32)