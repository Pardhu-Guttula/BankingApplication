# Epic Title: Banking Platform — Core API

class Layout:
    def __init__(self, name: str, components: list):
        self.name = name
        self.components = components

    def add_component(self, component: object):
        self.components.append(component)

    def remove_component(self, component: object):
        self.components.remove(component)

    def get_components(self) -> list:
        return self.components