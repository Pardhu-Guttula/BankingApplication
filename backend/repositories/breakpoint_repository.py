# Epic Title: Banking Platform — Core API

from backend.models.breakpoint import Breakpoint
import mysql.connector
from mysql.connector import pooling

class BreakpointRepository:
    def __init__(self):
        self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name="mypool",
            pool_size=5,
            host="localhost",
            user="root",
            password="password",
            database="banking"
        )

    def save_breakpoint(self, breakpoint: Breakpoint) -> None:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO breakpoint (name, min_width, max_width) VALUES (%s, %s, %s)",
            (breakpoint.name, breakpoint.get_min_width(), breakpoint.get_max_width())
        )
        conn.commit()
        cursor.close()
        conn.close()

    def get_breakpoints_by_layout_name(self, layout_name: str) -> list:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM breakpoint WHERE layout_name = %s", (layout_name,))
        breakpoints = [Breakpoint(
            name=row['name'], 
            min_width=row['min_width'],
            max_width=row['max_width']
        ) for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return breakpoints