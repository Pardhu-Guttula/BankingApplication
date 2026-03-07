# Epic Title: Banking Platform — Core API

from backend.models.side_navigation import SideNavigation
from backend.models.menu_item import MenuItem
from backend.repositories.menu_item_repository import MenuItemRepository
import mysql.connector
from mysql.connector import pooling

class SideNavigationRepository:
    def __init__(self):
        self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name="mypool",
            pool_size=5,
            host="localhost",
            user="root",
            password="password",
            database="banking"
        )
        self.menu_item_repository = MenuItemRepository()

    def save_side_navigation(self, side_navigation: SideNavigation) -> None:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO side_navigation (name, collapsed) VALUES (%s, %s)", 
                       (side_navigation.name, side_navigation.is_collapsed()))
        side_navigation_id = cursor.lastrowid
        conn.commit()
        cursor.close()
        conn.close()
        for item in side_navigation.get_items():
            self.menu_item_repository.save_menu_item(item)

    def get_side_navigation(self, name: str) -> SideNavigation:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM side_navigation WHERE name = %s", (name,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row:
            items = self.menu_item_repository.get_menu_items()
            side_navigation = SideNavigation(name=row['name'], items=items)
            side_navigation.collapsed = row['collapsed']
            return side_navigation
        return None