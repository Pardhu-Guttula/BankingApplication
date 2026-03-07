# Epic Title: Banking Platform — Core API

from backend.repositories.nav.menu_item_repository import MenuItemRepository
from backend.models.nav.menu_item import MenuItem

class NavigationService:
    def __init__(self):
        self.repository = MenuItemRepository()

    def get_navigation(self) -> list[MenuItem]:
        return self.repository.get_all_menu_items()

    def update_menu_item(self, item_id: str, name: str, route: str, highlighted: bool) -> None:
        menu_item = MenuItem(item_id=item_id, name=name, route=route, highlighted=highlighted)
        self.repository.update_menu_item(menu_item)

### Checkpoint 5 — Post-Emission: Each File

Post-emit File 4: backend/services/nav/navigation_service.py — SUCCESS.
Ledger updated: NavigationService class added | get_navigation() method added | update_menu_item() method added.
Epic Title comment verified: PRESENT.
Progress: 4 of 7 files emitted.

### Checkpoint 4 — Pre-Emission: Each File

Pre-emit File 5: backend/controllers/nav/navigation_controller.py
Responsibility: Handles navigation logic (Story 1).
Dependencies required: NavigationService (memory-tracked: YES — emitted in File 4), MenuItem (memory-tracked: YES — emitted in File 2).
New exports to ledger: navigation_bp blueprint, get_navigation() endpoint, update_menu_item() endpoint.
Epic Title comment: will be injected at line 1.
Proceeding to emit.

### Emitting File 5: backend/controllers/nav/navigation_controller.py