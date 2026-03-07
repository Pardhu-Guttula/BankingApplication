# Epic Title: Banking Platform — Core API

import mysql.connector
from mysql.connector import pooling
from backend.models.notifications.delivery_receipt import DeliveryReceipt
from backend.models.notifications.email_status import EmailStatus

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

    def get_email_status(self, email_id: str) -> EmailStatus:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT email_id, status FROM email_statuses WHERE email_id = %s", (email_id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return EmailStatus(email_id=row[0], status=row[1]) if row else None

    def save_delivery_receipt(self, receipt: DeliveryReceipt) -> None:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO delivery_receipts (receipt_id, email, status) VALUES (%s, %s, %s)",
            (receipt.receipt_id, receipt.email, receipt.status)
        )
        conn.commit()
        cursor.close()
        conn.close()

    def update_email_status(self, email_id: str, status: str) -> None:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE email_statuses SET status = %s WHERE email_id = %s",
            (status, email_id)
        )
        conn.commit()
        cursor.close()
        conn.close()