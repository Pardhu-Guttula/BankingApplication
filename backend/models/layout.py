# Epic Title: Banking Platform — Core API

from typing import List
from backend.models.component import Component

class Layout:
    def __init__(self, name: str, components: List[Component]):
        self.name = name
        self.components = components

    def add_component(self, component: Component):
        self.components.append(component)

    def remove_component(self, component: Component):
        self.components.remove(component)

    def get_components(self) -> List[Component]:
        return self.components

    def align_components(self):
        self.components.sort(key=lambda component: component.get_position())

    def check_consistency(self) -> bool:
        if not self.components:
            return True
        
        first_component = self.components[0]
        for component in self.components[1:]:
            if (component.margin != first_component.margin or
                component.padding != first_component.padding or
                component.font_style != first_component.font_style):
                return False
        return True