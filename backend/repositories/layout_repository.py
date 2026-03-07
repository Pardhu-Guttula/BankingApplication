# Epic Title: Banking Platform — Core API

from backend.models.layout import Layout
from backend.models.component import Component
from backend.models.breakpoint import Breakpoint
from backend.repositories.component_repository import ComponentRepository
from backend.repositories.breakpoint_repository import BreakpointRepository
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
        self.breakpoint_repository = BreakpointRepository()

    def save_layout(self, layout: Layout) -> None:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO layout (name) VALUES (%s)", (layout.name,))
        conn.commit()
        cursor.close()
        conn.close()
        for component in layout.get_components():
            self.component_repository.save_component(component)
        for breakpoint in layout.get_breakpoints():
            self.breakpoint_repository.save_breakpoint(breakpoint)

    def get_layout_by_name(self, name: str) -> Layout:
        components = self.component_repository.get_components_by_layout_name(name)
        breakpoints = self.breakpoint_repository.get_breakpoints_by_layout_name(name)
        if components and breakpoints:
            return Layout(name=name, components=components, breakpoints=breakpoints)
        return None