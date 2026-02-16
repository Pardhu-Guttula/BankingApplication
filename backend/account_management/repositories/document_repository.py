# Epic Title: Upload Documentation for Account Requests

from backend.account_management.models.document import Document
from backend.database import db

class DocumentRepository:

    def save_document_info(self, user_id: int, filename: str) -> Document:
        document = Document(user_id=user_id, filename=filename)
        db.session.add(document)
        db.session.commit()
        return document