# Epic Title: Banking Platform — Core API

from backend.repositories.layout_repository import LayoutRepository
from backend.models.layout import Layout

class LayoutService:
    def __init__(self, repository: LayoutRepository):
        self.repository = repository
    
    def create_layout(self, name: str, components: list):
        layout = Layout(name=name, components=components)
        self.repository.save_layout(layout)
    
    def get_layout(self, name: str) -> Layout:
        return self.repository.get_layout_by_name(name)