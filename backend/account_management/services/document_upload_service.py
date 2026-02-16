# Epic Title: Upload Documentation for Account Requests

import os
from backend.account_management.repositories.document_repository import DocumentRepository

class DocumentUploadService:
    def __init__(self):
        self.upload_folder = '/path/to/upload/folder'
        self.document_repository = DocumentRepository()

    def save_document_metadata(self, filename: str, file_path: str) -> bool:
        try:
            self.document_repository.save_document_metadata(filename, file_path)
            return True
        except Exception as e:
            return False