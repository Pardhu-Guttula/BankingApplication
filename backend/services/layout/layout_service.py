# Epic Title: Banking Platform — Core API

from backend.repositories.layout.layout_repository import LayoutRepository
from backend.models.layout.layout import Layout

class LayoutService:
    def __init__(self):
        self.repository = LayoutRepository()

    def adapt_layout(self, device_type: str):
        # Logic to adapt layout based on device_type
        pass

    def get_layout(self, layout_id: str) -> Layout:
        return self.repository.get_layout(layout_id)

    def add_layout(self, layout_id: str, device_type: str) -> Layout:
        layout = Layout(layout_id, device_type)
        self.repository.save_layout(layout)
        return layout