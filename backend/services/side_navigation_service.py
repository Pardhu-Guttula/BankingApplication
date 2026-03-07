# Epic Title: Banking Platform — Core API

from backend.repositories.side_navigation_repository import SideNavigationRepository
from backend.models.side_navigation import SideNavigation
from backend.models.menu_item import MenuItem

class SideNavigationService:
    def __init__(self, repository: SideNavigationRepository):
        self.repository = repository

    def create_side_navigation(self, name: str, items: list):
        item_objects = [MenuItem(
            name=item["name"],
            url=item["url"],
            category=item["category"],
            sub_items=[MenuItem(
                name=sub["name"],
                url=sub["url"],
                category=''
            ) for sub in item.get("sub_items", [])]
        ) for item in items]

        side_navigation = SideNavigation(name=name, items=item_objects)
        self.repository.save_side_navigation(side_navigation)

    def get_side_navigation(self, name: str) -> SideNavigation:
        return self.repository.get_side_navigation(name)