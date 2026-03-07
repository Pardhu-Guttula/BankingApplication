# Epic Title: Banking Platform — Core API

from backend.repositories.layout_repository import LayoutRepository
from backend.models.layout import Layout
from backend.models.component import Component
from backend.models.breakpoint import Breakpoint

class LayoutService:
    def __init__(self, repository: LayoutRepository):
        self.repository = repository

    def create_layout(self, name: str, components: list, breakpoints: list):
        component_objects = [Component(
            name=comp["name"], 
            position=comp["position"],
            margin=comp["margin"],
            padding=comp["padding"],
            font_style=comp["font_style"]
        ) for comp in components]

        breakpoint_objects = [Breakpoint(
            name=bp["name"], 
            min_width=bp["min_width"],
            max_width=bp["max_width"]
        ) for bp in breakpoints]

        layout = Layout(name=name, components=component_objects, breakpoints=breakpoint_objects)
        self.repository.save_layout(layout)

    def get_layout(self, name: str) -> Layout:
        layout = self.repository.get_layout_by_name(name)
        if layout:
            layout.align_components()
        return layout