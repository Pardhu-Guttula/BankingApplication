# Epic Title: Banking Platform — Core API

from backend.models.service_modifications.modification_request import ModificationRequest
import mysql.connector
from mysql.connector import pooling

class ModificationRequestRepository:
    def __init__(self):
        self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name="mypool",
            pool_size=5,
            host="localhost",
            user="root",
            password="password",
            database="banking"
        )

    def save_modification_request(self, modification_request: ModificationRequest) -> None:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO modification_requests (request_id, user_id, modification_type, data) VALUES (%s, %s, %s, %s)",
            (modification_request.request_id, modification_request.user_id, modification_request.modification_type, str(modification_request.data))
        )
        conn.commit()
        cursor.close()
        conn.close()