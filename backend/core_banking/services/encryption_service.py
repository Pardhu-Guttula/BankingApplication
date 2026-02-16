# Epic Title: Implement Data Encryption Protocols

from backend.core_banking.repositories.encryption_repository import EncryptionRepository

class EncryptionService:

    @staticmethod
    def encrypt_and_store_data(user_id: int, plain_data: str, password: str):
        EncryptionRepository.save_encrypted_data(user_id, plain_data, password)

    @staticmethod
    def retrieve_and_decrypt_data(user_id: int, record_id: int, password: str) -> str:
        return EncryptionRepository.get_decrypted_data(user_id, record_id, password)