# Epic Title: Upload Documentation for Account Requests

import os
from werkzeug.utils import secure_filename
from backend.account_management.repositories.document_repository import DocumentRepository

class DocumentService:
    def __init__(self):
        self.document_repository = DocumentRepository()

    def save_document(self, document, user_id: int, upload_folder: str) -> str:
        filename = secure_filename(f"{user_id}_{document.filename}")
        document.save(os.path.join(upload_folder, filename))
        self.document_repository.save_document(user_id, filename)
        return filename