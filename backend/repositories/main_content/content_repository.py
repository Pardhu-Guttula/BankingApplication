# Epic Title: Banking Platform — Core API

import mysql.connector
from mysql.connector import pooling
from backend.models.main_content.content import Content

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

    def get_content(self, content_id: str) -> Content:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT content_id, title, body FROM contents WHERE content_id = %s", (content_id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return Content(content_id=row[0], title=row[1], body=row[2]) if row else None

    def save_content(self, content: Content) -> None:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO contents (content_id, title, body) VALUES (%s, %s, %s)",
            (content.content_id, content.title, content.body)
        )
        conn.commit()
        cursor.close()
        conn.close()