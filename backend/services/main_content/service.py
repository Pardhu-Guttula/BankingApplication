# Epic Title: Banking Platform — Core API

from backend.repositories.main_content.repository import MainContentRepository
from backend.models.content_area import ContentArea
from backend.models.section import Section
from backend.models.information import Information

class MainContentService:
    def __init__(self, repository: MainContentRepository):
        self.repository = repository
    
    def get_main_content(self, section: Section) -> ContentArea:
        return self.repository.get_content_area(section)
    
    def get_section_information(self, section: Section) -> Information:
        return self.repository.get_information(section)