# Epic Title: Banking Platform — Core API

class Breakpoint:
    def __init__(self, name: str, min_width: int, max_width: int):
        self.name = name
        self.min_width = min_width
        self.max_width = max_width

    def set_min_width(self, min_width: int):
        self.min_width = min_width

    def set_max_width(self, max_width: int):
        self.max_width = max_width

    def get_min_width(self) -> int:
        return self.min_width

    def get_max_width(self) -> int:
        return self.max_width