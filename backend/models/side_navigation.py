# Epic Title: Banking Platform — Core API

from typing import List
from backend.models.menu_item import MenuItem

class SideNavigation:
    def __init__(self, name: str, items: List[MenuItem]):
        self.name = name
        self.items = items
        self.collapsed = False

    def add_item(self, item: MenuItem):
        self.items.append(item)

    def remove_item(self, item: MenuItem):
        self.items.remove(item)

    def get_items(self) -> List[MenuItem]:
        return self.items

    def toggle_collapse(self):
        self.collapsed = not self.collapsed

    def is_collapsed(self) -> bool:
        return self.collapsed