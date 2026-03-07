# Epic Title: Banking Platform — Core API

from backend.repositories.header.header_repository import HeaderRepository
from backend.models.header.header_menu import HeaderMenu, HeaderLink

class HeaderService:
    def __init__(self):
        self.repository = HeaderRepository()

    def create_header_menu(self, title: str, links: list):
        link_objects = [HeaderLink(
            name=link["name"],
            url=link["url"]
        ) for link in links]

        header_menu = HeaderMenu(title=title, links=link_objects)
        self.repository.save_header_menu(header_menu)

    def get_header_menu(self) -> HeaderMenu:
        return self.repository.get_header_menu()