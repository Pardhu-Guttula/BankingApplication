# Epic Title: Banking Platform — Core API

from backend.repositories.main_content.content_repository import ContentRepository
from backend.models.main_content.content import Content

class ContentService:
    def __init__(self):
        self.repository = ContentRepository()

    def get_content(self, content_id: str) -> Content:
        return self.repository.get_content(content_id)

    def add_content(self, content_id: str, title: str, body: str) -> Content:
        content = Content(content_id, title, body)
        self.repository.save_content(content)
        return content