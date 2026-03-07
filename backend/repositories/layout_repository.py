# Epic Title: Banking Platform — Core API

from backend.models.layout import Layout
import mysql.connector
from mysql.connector import pooling

class LayoutRepository:
    def __init__(self):
        self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name="mypool",
            pool_size=5,
            host="localhost",
            user="root",
            password="password",
            database="banking"
        )

    def save_layout(self, layout: Layout) -> None:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO layout (name, components) VALUES (%s, %s)", (layout.name, str(layout.components)))
        conn.commit()
        cursor.close()
        conn.close()

    def get_layout_by_name(self, name: str) -> Layout:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM layout WHERE name = %s", (name,))
        layout_row = cursor.fetchone()
        cursor.close()
        conn.close()
        if layout_row:
            return Layout(name=layout_row["name"], components=eval(layout_row["components"]))
        return None