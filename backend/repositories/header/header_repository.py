# Epic Title: Banking Platform — Core API

from backend.models.header.header_menu import HeaderMenu, HeaderLink
import mysql.connector
from mysql.connector import pooling

class HeaderRepository:
    def __init__(self):
        self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name="mypool",
            pool_size=5,
            host="localhost",
            user="root",
            password="password",
            database="banking"
        )

    def save_header_menu(self, header_menu: HeaderMenu) -> None:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO header_menu (title) VALUES (%s)",
            (header_menu.title,)
        )
        header_menu_id = cursor.lastrowid
        conn.commit()
        cursor.close()
        conn.close()
        for link in header_menu.get_links():
            self.save_header_link(header_menu_id, link)

    def save_header_link(self, header_menu_id: int, link: HeaderLink) -> None:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO header_link (header_menu_id, name, url) VALUES (%s, %s, %s)",
            (header_menu_id, link.name, link.url)
        )
        conn.commit()
        cursor.close()
        conn.close()

    def get_header_menu(self) -> HeaderMenu:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM header_menu LIMIT 1")
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row:
            links = self.get_header_links(row['id'])
            header_menu = HeaderMenu(title=row['title'], links=links)
            return header_menu
        return None

    def get_header_links(self, header_menu_id: int) -> list:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM header_link WHERE header_menu_id = %s", (header_menu_id,))
        links = [HeaderLink(
            name=row['name'],
            url=row['url']
        ) for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return links