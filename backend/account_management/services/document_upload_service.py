# Epic Title: Upload Documentation for Account Requests

from backend.account_management.repositories.document_repository import DocumentRepository

class DocumentUploadService:
    def __init__(self):
        self.document_repository = DocumentRepository()

    def save_document_info(self, user_id: int, filename: str) -> bool:
        try:
            self.document_repository.save_document_info(user_id, filename)
            return True
        except Exception:
            return False