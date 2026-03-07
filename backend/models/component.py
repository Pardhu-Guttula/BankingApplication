# Epic Title: Banking Platform — Core API

class Component:
    def __init__(self, name: str, position: int):
        self.name = name
        self.position = position

    def set_position(self, position: int):
        self.position = position

    def get_position(self) -> int:
        return self.position