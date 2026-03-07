# Epic Title: Banking Platform — Core API

from backend.models.component import Component
import mysql.connector
from mysql.connector import pooling

class ComponentRepository:
    def __init__(self):
        self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name="mypool",
            pool_size=5,
            host="localhost",
            user="root",
            password="password",
            database="banking"
        )

    def save_component(self, component: Component) -> None:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO component (name, position) VALUES (%s, %s)", (component.name, component.get_position()))
        conn.commit()
        cursor.close()
        conn.close()

    def get_components_by_layout_name(self, layout_name: str) -> list:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM component WHERE layout_name = %s", (layout_name,))
        components = [Component(name=row['name'], position=row['position']) for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return components