# Epic Title: Banking Platform — Core API

from backend.repositories.header.header_repository import HeaderRepository
from backend.models.header.header_element import HeaderElement

class HeaderService:
    def __init__(self):
        self.repository = HeaderRepository()

    def get_header_elements(self) -> list[HeaderElement]:
        return self.repository.get_header_elements()

    def add_header_element(self, element_id: str, content: str) -> HeaderElement:
        header_element = HeaderElement(element_id, content)
        self.repository.save_header_element(header_element)
        return header_element