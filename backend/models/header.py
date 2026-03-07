# Epic Title: Banking Platform — Core API

from typing import List

class NavigationLink:
    def __init__(self, name: str, url: str):
        self.name = name
        self.url = url

class Header:
    def __init__(self, title: str, links: List[NavigationLink]):
        self.title = title
        self.links = links

    def add_link(self, link: NavigationLink):
        self.links.append(link)

    def remove_link(self, link: NavigationLink):
        self.links.remove(link)

    def get_links(self) -> List[NavigationLink]:
        return self.links