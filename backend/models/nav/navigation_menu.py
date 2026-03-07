# Epic Title: Banking Platform — Core API

from typing import List

class NavigationLink:
    def __init__(self, name: str, url: str, icon: str):
        self.name = name
        self.url = url
        self.icon = icon

class NavigationMenu:
    def __init__(self, links: List[NavigationLink]):
        self.links = links
        self.expanded = True
        self.active_link = None

    def expand(self):
        self.expanded = True

    def collapse(self):
        self.expanded = False

    def set_active_link(self, link: NavigationLink):
        self.active_link = link

    def get_active_link(self) -> NavigationLink:
        return self.active_link

    def toggle(self):
        self.expanded = not self.expanded

    def get_links(self) -> List[NavigationLink]:
        return self.links