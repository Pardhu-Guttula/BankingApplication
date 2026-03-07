# Epic Title: Banking Platform — Core API

import mysql.connector
from mysql.connector import pooling
from backend.models.notifications.delivery_receipt import DeliveryReceipt
from backend.models.notifications.email_template import EmailTemplate

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

    def get_email_template(self, template_id: str) -> EmailTemplate:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT template_id, subject, body FROM email_templates WHERE template_id = %s", (template_id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return EmailTemplate(template_id=row[0], subject=row[1], body=row[2]) if row else None

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