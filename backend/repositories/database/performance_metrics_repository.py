# Epic Title: Banking Platform — Core API

from backend.models.performance_metrics import PerformanceMetrics
import mysql.connector
from mysql.connector import pooling
from datetime import datetime

class PerformanceMetricsRepository:
    def __init__(self):
        self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name="mypool",
            pool_size=5,
            host="localhost",
            user="root",
            password="password",
            database="banking"
        )

    def save_performance_metrics(self, metrics: PerformanceMetrics) -> None:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO performance_metrics (metrics_id, operation, duration, timestamp) VALUES (%s, %s, %s, %s)",
            (metrics.metrics_id, metrics.operation, metrics.duration, metrics.timestamp)
        )
        conn.commit()
        cursor.close()
        conn.close()

    def get_performance_metrics(self) -> list:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM performance_metrics")
        metrics = [PerformanceMetrics(
            metrics_id=row['metrics_id'],
            operation=row['operation'],
            duration=row['duration'],
            timestamp=row['timestamp']
        ) for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return metrics