# Epic Title: Banking Platform — Core API

from backend.models.main_content_area import MainContentArea, MainContentView
import mysql.connector
from mysql.connector import pooling

class MainContentRepository:
    def __init__(self):
        self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name="mypool",
            pool_size=5,
            host="localhost",
            user="root",
            password="password",
            database="banking"
        )

    def save_main_content_area(self, main_content_area: MainContentArea) -> None:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO main_content_area (current_view) VALUES (%s)",
            (main_content_area.get_current_view().name if main_content_area.get_current_view() else None,)
        )
        main_content_area_id = cursor.lastrowid
        conn.commit()
        cursor.close()
        conn.close()
        for view in main_content_area.get_views():
            self.save_main_content_view(main_content_area_id, view)

    def save_main_content_view(self, main_content_area_id: int, view: MainContentView) -> None:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO main_content_view (main_content_area_id, name, content) VALUES (%s, %s, %s)",
            (main_content_area_id, view.name, view.content)
        )
        conn.commit()
        cursor.close()
        conn.close()

    def get_main_content_area(self) -> MainContentArea:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM main_content_area LIMIT 1")
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row:
            views = self.get_main_content_views(row['id'])
            main_content_area = MainContentArea(views=views)
            return main_content_area
        return None

    def get_main_content_views(self, main_content_area_id: int) -> list:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM main_content_view WHERE main_content_area_id = %s", (main_content_area_id,))
        views = [MainContentView(
            name=row['name'],
            content=row['content']
        ) for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return views