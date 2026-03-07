# Epic Title: Banking Platform — Core API

import mysql.connector
from mysql.connector import pooling
from backend.models.dashboard.dashboard import Dashboard

class DashboardRepository:
    def __init__(self):
        self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name="mypool",
            pool_size=5,
            host="localhost",
            user="root",
            password="password",
            database="banking"
        )

    def get_dashboard(self, dashboard_id: str) -> Dashboard:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT dashboard_id, name FROM dashboards WHERE dashboard_id = %s", (dashboard_id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return Dashboard(dashboard_id=row[0], name=row[1]) if row else None

    def save_dashboard(self, dashboard: Dashboard) -> None:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO dashboards (dashboard_id, name) VALUES (%s, %s)",
            (dashboard.dashboard_id, dashboard.name)
        )
        conn.commit()
        cursor.close()
        conn.close()