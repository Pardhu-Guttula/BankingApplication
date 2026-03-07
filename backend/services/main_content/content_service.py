# Epic Title: Banking Platform — Core API

from backend.repositories.main_content.content_repository import ContentRepository
from backend.models.main_content.content_element import ContentElement

class ContentService:
    def __init__(self):
        self.repository = ContentRepository()

    def get_content_elements(self) -> list[ContentElement]:
        return self.repository.get_content_elements()

    def add_content_element(self, element_id: str, content: str) -> ContentElement:
        content_element = ContentElement(element_id, content)
        self.repository.save_content_element(content_element)
        return content_element