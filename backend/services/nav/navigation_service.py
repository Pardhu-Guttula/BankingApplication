# Epic Title: Banking Platform — Core API

from backend.repositories.nav.navigation_repository import NavigationRepository
from backend.models.nav.navigation_menu import NavigationMenu, NavigationLink

class NavigationService:
    def __init__(self):
        self.repository = NavigationRepository()

    def create_navigation_menu(self, links: list):
        link_objects = [NavigationLink(
            name=link["name"],
            url=link["url"],
            icon=link["icon"]
        ) for link in links]

        navigation_menu = NavigationMenu(links=link_objects)
        self.repository.save_navigation_menu(navigation_menu)

    def get_navigation_menu(self) -> NavigationMenu:
        return self.repository.get_navigation_menu()

    def toggle_navigation_menu(self):
        menu = self.repository.get_navigation_menu()
        menu.toggle()
        self.repository.save_navigation_menu(menu)

    def set_active_link(self, active_link: NavigationLink):
        menu = self.repository.get_navigation_menu()
        menu.set_active_link(active_link)
        self.repository.save_navigation_menu(menu)