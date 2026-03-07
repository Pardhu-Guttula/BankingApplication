# Epic Title: Banking Platform — Core API

from backend.models.menu_item import MenuItem
import mysql.connector
from mysql.connector import pooling

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

    def save_menu_item(self, menu_item: MenuItem) -> None:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO menu_item (name, url, category) VALUES (%s, %s, %s)",
            (menu_item.name, menu_item.url, menu_item.category)
        )
        menu_item_id = cursor.lastrowid
        conn.commit()
        cursor.close()
        conn.close()
        for sub_item in menu_item.sub_items:
            self.save_sub_item(menu_item_id, sub_item)

    def save_sub_item(self, parent_id: int, sub_item: MenuItem) -> None:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO sub_menu_item (parent_id, name, url) VALUES (%s, %s, %s)",
            (parent_id, sub_item.name, sub_item.url)
        )
        conn.commit()
        cursor.close()
        conn.close()

    def get_menu_items(self) -> list:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM menu_item")
        menu_items = []
        for row in cursor.fetchall():
            item = MenuItem(
                name=row['name'],
                url=row['url'],
                category=row['category'],
                sub_items=self.get_sub_items(row['id'])
            )
            menu_items.append(item)
        cursor.close()
        conn.close()
        return menu_items

    def get_sub_items(self, parent_id: int) -> list:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM sub_menu_item WHERE parent_id = %s", (parent_id,))
        sub_items = [MenuItem(
            name=row['name'],
            url=row['url'],
            category=''  # Sub-items don't have categories
        ) for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return sub_items