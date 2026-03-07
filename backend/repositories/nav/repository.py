# Epic Title: Banking Platform — Core API

from backend.models.navigation import Navigation
from backend.models.section import Section
from backend.models.icon import Icon

class NavRepository:
    def get_all(self) -> list:
        # Retrieve all available navigation items
        pass
    
    def get_sections(self) -> list:
        # Retrieve all sections
        pass
    
    def get_icon(self, name: str) -> Icon:
        # Retrieve icon by name
        pass