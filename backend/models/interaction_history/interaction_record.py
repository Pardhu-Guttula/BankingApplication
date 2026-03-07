# Epic Title: Banking Platform — Core API

from Crypto.Cipher import AES
import base64
import hashlib

class InteractionRecord:
    def __init__(self, interaction_id: str, user_id: str, interaction_type: str, timestamp: str, location: str):
        self.interaction_id = interaction_id
        self.user_id = user_id
        self.interaction_type = interaction_type
        self.timestamp = timestamp
        self.location = location

    def encrypt_data(self, key: str) -> 'InteractionRecord':
        cipher = AES.new(hashlib.sha256(key.encode()).digest(), AES.MODE_EAX)
        nonce = cipher.nonce
        ciphertext, _ = cipher.encrypt_and_digest(f"{self.interaction_id},{self.user_id},{self.interaction_type},{self.timestamp},{self.location}".encode())
        encrypted_data = base64.b64encode(nonce + ciphertext).decode()
        return InteractionRecord(encrypted_data, encrypted_data, encrypted_data, encrypted_data, encrypted_data)

    def decrypt_data(self, key: str) -> 'InteractionRecord':
        encrypted_values = self.interaction_id.split(',')
        nonce = base64.b64decode(encrypted_values[0].encode())
        ciphertext = base64.b64decode(encrypted_values[1].encode())
        cipher = AES.new(hashlib.sha256(key.encode()).digest(), AES.MODE_EAX, nonce=nonce)
        plaintext = cipher.decrypt(ciphertext).decode().split(',')
        decrypted_record = InteractionRecord(plaintext[0], plaintext[1], plaintext[2], plaintext[3], plaintext[4])
        return decrypted_record