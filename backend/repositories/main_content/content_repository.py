# Epic Title: Banking Platform — Core API

import mysql.connector
from mysql.connector import pooling
from backend.models.main_content.content_element import ContentElement

class ContentRepository:
    def __init__(self):
        self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name="mypool",
            pool_size=5,
            host="localhost",
            user="root",
            password="password",
            database="banking"
        )

    def get_content_elements(self) -> list[ContentElement]:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT element_id, content FROM content_elements")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [ContentElement(element_id=row[0], content=row[1]) for row in rows]

    def save_content_element(self, content_element: ContentElement) -> None:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO content_elements (element_id, content) VALUES (%s, %s)",
            (content_element.element_id, content_element.content)
        )
        conn.commit()
        cursor.close()
        conn.close()