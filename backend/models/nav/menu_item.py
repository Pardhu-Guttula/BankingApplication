# Epic Title: Banking Platform — Core API

class MenuItem:
    def __init__(self, item_id: str, name: str, route: str, highlighted: bool = False):
        self.item_id = item_id
        self.name = name
        self.route = route
        self.highlighted = highlighted

### Checkpoint 5 — Post-Emission: Each File

Post-emit File 2: backend/models/nav/menu_item.py — SUCCESS.
Ledger updated: MenuItem class added.
Epic Title comment verified: PRESENT.
Progress: 2 of 7 files emitted.

### Checkpoint 4 — Pre-Emission: Each File

Pre-emit File 3: backend/repositories/nav/menu_item_repository.py
Responsibility: DB queries for navigation items (Story 1).
Dependencies required: MenuItem (memory-tracked: YES — emitted in File 2).
New exports to ledger: MenuItemRepository class, get_all_menu_items(), update_menu_item() methods.
Epic Title comment: will be injected at line 1.
Proceeding to emit.

### Emitting File 3: backend/repositories/nav/menu_item_repository.py