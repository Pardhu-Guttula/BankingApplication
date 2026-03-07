# Epic Title: Banking Platform — Core API

from backend.models.header import Header, NavigationLink
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

    def save_header(self, header: Header) -> None:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO header (title) VALUES (%s)",
            (header.title,)
        )
        header_id = cursor.lastrowid
        conn.commit()
        cursor.close()
        conn.close()
        for link in header.get_links():
            self.save_navigation_link(header_id, link)

    def save_navigation_link(self, header_id: int, link: NavigationLink) -> None:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO navigation_link (header_id, name, url) VALUES (%s, %s, %s)",
            (header_id, link.name, link.url)
        )
        conn.commit()
        cursor.close()
        conn.close()

    def get_header(self, title: str) -> Header:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM header WHERE title = %s", (title,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row:
            links = self.get_navigation_links(row['id'])
            header = Header(title=row['title'], links=links)
            return header
        return None

    def get_navigation_links(self, header_id: int) -> list:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM navigation_link WHERE header_id = %s", (header_id,))
        links = [NavigationLink(
            name=row['name'],
            url=row['url']
        ) for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return links