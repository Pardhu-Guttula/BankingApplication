# Epic Title: Banking Platform — Core API

import mysql.connector
from mysql.connector import pooling
from backend.models.auth.log import Log

class LogRepository:
    def __init__(self):
        self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name="mypool",
            pool_size=5,
            host="localhost",
            user="root",
            password="password",
            database="banking"
        )

    def save_log(self, log: Log) -> None:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO logs (log_id, user_id, action, timestamp, details) VALUES (%s, %s, %s, %s, %s)",
            (log.log_id, log.user_id, log.action, log.timestamp, log.details)
        )
        conn.commit()
        cursor.close()
        conn.close()

    def get_logs(self, action: str = None) -> list[Log]:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        if action:
            cursor.execute("SELECT log_id, user_id, action, timestamp, details FROM logs WHERE action = %s", (action,))
        else:
            cursor.execute("SELECT log_id, user_id, action, timestamp, details FROM logs")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [Log(log_id=row[0], user_id=row[1], action=row[2], timestamp=row[3], details=row[4]) for row in rows]