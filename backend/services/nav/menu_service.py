# Epic Title: Banking Platform — Core API

from backend.repositories.nav.menu_repository import MenuRepository
from backend.models.nav.menu_item import MenuItem

class MenuService:
    def __init__(self):
        self.repository = MenuRepository()

    def get_menu_items(self, user_role: str) -> list[MenuItem]:
        return self.repository.get_menu_items(user_role)

    def add_menu_item(self, item_id: str, name: str, role: str) -> MenuItem:
        menu_item = MenuItem(item_id, name, role)
        self.repository.save_menu_item(menu_item)
        return menu_item