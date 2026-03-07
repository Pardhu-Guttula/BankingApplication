# Epic Title: Banking Platform — Core API

from backend.repositories.header.navigation_link_repository import NavigationLinkRepository
from backend.models.header.navigation_link import NavigationLink

class HeaderService:
    def __init__(self):
        self.repository = NavigationLinkRepository()

    def get_navigation_links(self) -> list[NavigationLink]:
        return self.repository.get_all_links()

    def update_navigation_link(self, link_id: str, name: str, route: str, key_functionality: bool) -> None:
        navigation_link = NavigationLink(link_id=link_id, name=name, route=route, key_functionality=key_functionality)
        self.repository.update_link(navigation_link)