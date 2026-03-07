# Epic Title: Banking Platform — Core API

class Component:
    def __init__(self, name: str, position: int, margin: str, padding: str, font_style: str, alignment: str):
        self.name = name
        self.position = position
        self.margin = margin
        self.padding = padding
        self.font_style = font_style
        self.alignment = alignment

    def set_position(self, position: int):
        self.position = position

    def get_position(self) -> int:
        return self.position

    def set_margin(self, margin: str):
        self.margin = margin

    def set_padding(self, padding: str):
        self.padding = padding

    def set_font_style(self, font_style: str):
        self.font_style = font_style

    def set_alignment(self, alignment: str):
        self.alignment = alignment

    def get_alignment(self) -> str:
        return self.alignment