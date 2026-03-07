# Epic Title: Banking Platform — Core API

from backend.models.nav.navigation_menu import NavigationMenu, NavigationLink
import mysql.connector
from mysql.connector import pooling

class NavigationRepository:
    def __init__(self):
        self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name="mypool",
            pool_size=5,
            host="localhost",
            user="root",
            password="password",
            database="banking"
        )

    def save_navigation_menu(self, navigation_menu: NavigationMenu) -> None:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        # Simplified to only save the state
        cursor.execute(
            "INSERT INTO navigation_menu (expanded) VALUES (%s)",
            (navigation_menu.expanded,)
        )
        navigation_menu_id = cursor.lastrowid
        conn.commit()
        cursor.close()
        conn.close()
        for link in navigation_menu.get_links():
            self.save_navigation_link(navigation_menu_id, link)

    def save_navigation_link(self, navigation_menu_id: int, link: NavigationLink) -> None:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO navigation_link (navigation_menu_id, name, url, icon) VALUES (%s, %s, %s, %s)",
            (navigation_menu_id, link.name, link.url, link.icon)
        )
        conn.commit()
        cursor.close()
        conn.close()

    def get_navigation_menu(self) -> NavigationMenu:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM navigation_menu LIMIT 1")
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row:
            links = self.get_navigation_links(row['id'])
            navigation_menu = NavigationMenu(links=links)
            navigation_menu.expanded = row['expanded']
            return navigation_menu
        return None

    def get_navigation_links(self, navigation_menu_id: int) -> list:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM navigation_link WHERE navigation_menu_id = %s", (navigation_menu_id,))
        links = [NavigationLink(
            name=row['name'],
            url=row['url'],
            icon=row['icon']
        ) for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return links