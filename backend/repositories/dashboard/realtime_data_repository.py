# Epic Title: Banking Platform — Core API

from backend.models.dashboard.dashboard import RealTimeData
import mysql.connector
from mysql.connector import pooling
from datetime import datetime

class RealTimeDataRepository:
    def __init__(self):
        self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name="mypool",
            pool_size=5,
            host="localhost",
            user="root",
            password="password",
            database="banking"
        )

    def save_realtime_data(self, realtime_data: RealTimeData) -> None:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO realtime_data (data_id, content, timestamp) VALUES (%s, %s, %s)",
            (realtime_data.data_id, realtime_data.content, realtime_data.timestamp)
        )
        conn.commit()
        cursor.close()
        conn.close()

    def get_latest_data(self) -> RealTimeData:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM realtime_data ORDER BY timestamp DESC LIMIT 1")
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row:
            realtime_data = RealTimeData(
                data_id=row['data_id'],
                content=row['content'],
                timestamp=row['timestamp']
            )
            return realtime_data
        return None