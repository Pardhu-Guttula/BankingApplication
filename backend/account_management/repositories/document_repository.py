# Epic Title: Upload Documentation for Account Requests

from backend.account_management.models.document import Document
from backend.database import db

class DocumentRepository:

    def save_document_metadata(self, filename: str, file_path: str) -> Document:
        document = Document(filename=filename, file_path=file_path)
        db.session.add(document)
        db.session.commit()
        return document