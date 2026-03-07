# Epic Title: Banking Platform — Core API

from backend.models.monitoring_dashboard import MonitoringDashboard
import mysql.connector
from mysql.connector import pooling

class MonitoringRepository:
    def __init__(self):
        self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name="mypool",
            pool_size=5,
            host="localhost",
            user="root",
            password="password",
            database="banking"
        )

    def save_alert(self, alert: str) -> None:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO monitoring_alerts (alert) VALUES (%s)",
            (alert,)
        )
        conn.commit()
        cursor.close()
        conn.close()

    def save_performance_report(self, report: str) -> None:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO monitoring_reports (report) VALUES (%s)",
            (report,)
        )
        conn.commit()
        cursor.close()
        conn.close()

    def get_alerts(self) -> list:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM monitoring_alerts")
        alerts = [row['alert'] for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return alerts

    def get_performance_reports(self) -> list:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM monitoring_reports")
        reports = [row['report'] for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return reports