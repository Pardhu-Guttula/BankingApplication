# Epic Title: Banking Platform — Core API

from backend.repositories.layout.layout_repository import LayoutRepository
from backend.models.layout.layout import Layout

class LayoutService:
    def __init__(self):
        self.repository = LayoutRepository()

    def get_layout(self, layout_id: str) -> Layout:
        return self.repository.get_layout(layout_id)

    def add_layout(self, layout_id: str, screen_size: str, breakpoint: str) -> Layout:
        layout = Layout(layout_id, screen_size, breakpoint)
        self.repository.save_layout(layout)
        return layout