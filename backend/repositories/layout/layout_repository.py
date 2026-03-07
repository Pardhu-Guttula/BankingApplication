# Epic Title: Banking Platform — Core API

import mysql.connector
from mysql.connector import pooling
from backend.models.layout.layout import Layout

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

    def get_layout(self, layout_id: str) -> Layout:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT layout_id, screen_size, breakpoint FROM layouts WHERE layout_id = %s", (layout_id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return Layout(layout_id=row[0], screen_size=row[1], breakpoint=row[2]) if row else None

    def save_layout(self, layout: Layout) -> None:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO layouts (layout_id, screen_size, breakpoint) VALUES (%s, %s, %s)",
            (layout.layout_id, layout.screen_size, layout.breakpoint)
        )
        conn.commit()
        cursor.close()
        conn.close()