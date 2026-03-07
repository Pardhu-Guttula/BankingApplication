# Epic Title: Banking Platform — Core API

from backend.models.service_request import ServiceRequest
import mysql.connector
from mysql.connector import pooling

class ServiceRequestRepository:
    def __init__(self):
        self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name="mypool",
            pool_size=5,
            host="localhost",
            user="root",
            password="password",
            database="banking"
        )

    def get_service_requests_by_user_id(self, user_id: int) -> list:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM service_request WHERE user_id = %s", (user_id,))
        requests = [ServiceRequest(**row) for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return requests

    def update_service_request_status(self, request_id: int, new_status: str) -> None:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE service_request SET status = %s WHERE request_id = %s", (new_status, request_id))
        conn.commit()
        cursor.close()
        conn.close()