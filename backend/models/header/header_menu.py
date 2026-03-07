# Epic Title: Banking Platform — Core API

from typing import List

class HeaderLink:
    def __init__(self, name: str, url: str):
        self.name = name
        self.url = url

class HeaderMenu:
    def __init__(self, title: str, links: List[HeaderLink]):
        self.title = title
        self.links = links

    def get_links(self) -> List[HeaderLink]:
        return self.links