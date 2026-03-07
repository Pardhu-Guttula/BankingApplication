# Epic Title: Banking Platform — Core API

import mysql.connector
from mysql.connector import pooling
from backend.models.notifications.notification import Notification

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

    def save_notification(self, notification: Notification) -> None:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO notifications (user_id, notification_type, message, timestamp) VALUES (%s, %s, %s, %s)",
            (notification.user_id, notification.notification_type, notification.message, notification.timestamp)
        )
        conn.commit()
        cursor.close()
        conn.close()

    def get_notifications(self, user_id: str) -> list[Notification]:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT user_id, notification_type, message, timestamp FROM notifications WHERE user_id = %s", (user_id,))
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [Notification(user_id=row[0], notification_type=row[1], message=row[2], timestamp=row[3]) for row in rows]