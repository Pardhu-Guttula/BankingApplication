# Epic Title: Banking Platform — Core API

from backend.models.layout import Layout
from backend.models.component import Component
from backend.repositories.component_repository import ComponentRepository
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
        self.component_repository = ComponentRepository()

    def save_layout(self, layout: Layout) -> None:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO layout (name) VALUES (%s)", (layout.name,))
        conn.commit()
        cursor.close()
        conn.close()
        for component in layout.get_components():
            self.component_repository.save_component(component)

    def get_layout_by_name(self, name: str) -> Layout:
        components = self.component_repository.get_components_by_layout_name(name)
        if components:
            return Layout(name=name, components=components)
        return None