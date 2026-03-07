# Epic Title: Banking Platform — Core API

import mysql.connector
from mysql.connector import pooling
from backend.models.notifications.update_notification import UpdateNotification

class NotificationRepository:
    def __init__(self):
        self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name="mypool",
            pool_size=5,
            host="localhost",
            user="root",
            password="password",
            database="banking"
        )

    def save_notification(self, notification: UpdateNotification) -> None:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO notifications (request_id, status, message) VALUES (%s, %s, %s)",
            (notification.request_id, notification.status, notification.message)
        )
        conn.commit()
        cursor.close()
        conn.close()