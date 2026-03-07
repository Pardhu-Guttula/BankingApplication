# Epic Title: Banking Platform — Core API

from backend.repositories.header_repository import HeaderRepository
from backend.models.header import Header, NavigationLink

class HeaderService:
    def __init__(self, repository: HeaderRepository):
        self.repository = repository

    def create_header(self, title: str, links: list):
        link_objects = [NavigationLink(
            name=link["name"],
            url=link["url"]
        ) for link in links]

        header = Header(title=title, links=link_objects)
        self.repository.save_header(header)

    def get_header(self, title: str) -> Header:
        return self.repository.get_header(title)