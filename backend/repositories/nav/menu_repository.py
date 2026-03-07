# Epic Title: Banking Platform — Core API

import mysql.connector
from mysql.connector import pooling
from backend.models.nav.menu_item import MenuItem

class MenuRepository:
    def __init__(self):
        self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name="mypool",
            pool_size=5,
            host="localhost",
            user="root",
            password="password",
            database="banking"
        )

    def get_menu_items(self, user_role: str) -> list[MenuItem]:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT item_id, name, role FROM menu_items WHERE role = %s", (user_role,))
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [MenuItem(item_id=row[0], name=row[1], role=row[2]) for row in rows]

    def save_menu_item(self, menu_item: MenuItem) -> None:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO menu_items (item_id, name, role) VALUES (%s, %s, %s)",
            (menu_item.item_id, menu_item.name, menu_item.role)
        )
        conn.commit()
        cursor.close()
        conn.close()