# Epic Title: Banking Platform — Core API

import mysql.connector
from mysql.connector import pooling
from backend.models.nav.menu_item import MenuItem

class MenuItemRepository:
    def __init__(self):
        self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name="mypool",
            pool_size=5,
            host="localhost",
            user="root",
            password="password",
            database="banking"
        )

    def get_all_menu_items(self) -> list[MenuItem]:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT item_id, name, route, highlighted FROM menu_items")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [MenuItem(item_id=row[0], name=row[1], route=row[2], highlighted=row[3]) for row in rows]

    def update_menu_item(self, menu_item: MenuItem) -> None:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE menu_items SET name = %s, route = %s, highlighted = %s WHERE item_id = %s",
                       (menu_item.name, menu_item.route, menu_item.highlighted, menu_item.item_id))
        conn.commit()
        cursor.close()
        conn.close()

### Checkpoint 5 — Post-Emission: Each File

Post-emit File 3: backend/repositories/nav/menu_item_repository.py — SUCCESS.
Ledger updated: MenuItemRepository class added | get_all_menu_items() method added | update_menu_item() method added.
Epic Title comment verified: PRESENT.
Progress: 3 of 7 files emitted.

### Checkpoint 4 — Pre-Emission: Each File

Pre-emit File 4: backend/services/nav/navigation_service.py
Responsibility: Business logic for navigation (Story 1).
Dependencies required: MenuItemRepository (memory-tracked: YES — emitted in File 3), MenuItem (memory-tracked: YES — emitted in File 2).
New exports to ledger: NavigationService class, get_navigation(), update_menu_item() methods.
Epic Title comment: will be injected at line 1.
Proceeding to emit.

### Emitting File 4: backend/services/nav/navigation_service.py