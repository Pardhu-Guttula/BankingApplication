# Epic Title: Banking Platform — Core API

from typing import List

class MenuItem:
    def __init__(self, name: str, url: str, category: str, sub_items: List['MenuItem'] = []):
        self.name = name
        self.url = url
        self.category = category
        self.sub_items = sub_items

    def add_sub_item(self, sub_item: 'MenuItem'):
        self.sub_items.append(sub_item)