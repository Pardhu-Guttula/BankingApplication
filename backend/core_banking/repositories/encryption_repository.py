# Epic Title: Implement Data Encryption Protocols

from backend.core_banking.models.encrypted_data_model import db, EncryptedFinancialData

class EncryptionRepository:

    @staticmethod
    def save_encrypted_data(user_id: int, plain_data: str, password: str):
        encrypted_data = EncryptedFinancialData.encrypt_data(plain_data, password)
        encrypted_record = EncryptedFinancialData(user_id=user_id, encrypted_data=encrypted_data)
        db.session.add(encrypted_record)
        db.session.commit()

    @staticmethod
    def get_decrypted_data(user_id: int, record_id: int, password: str) -> str:
        record = EncryptedFinancialData.query.filter_by(id=record_id, user_id=user_id).first()
        if record:
            return EncryptedFinancialData.decrypt_data(record.encrypted_data, password)
        return None