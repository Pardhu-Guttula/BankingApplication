# Epic Title: Banking Platform — Core API

from backend.models.user_request import UserRequest
import mysql.connector
from mysql.connector import pooling
from datetime import datetime

class UserRequestRepository:
    def __init__(self):
        self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name="mypool",
            pool_size=5,
            host="localhost",
            user="root",
            password="password",
            database="banking"
        )

    def save_user_request(self, user_request: UserRequest) -> None:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO user_request (request_id, user_id, operation, timestamp) VALUES (%s, %s, %s, %s)",
            (user_request.request_id, user_request.user_id, user_request.operation, user_request.timestamp)
        )
        conn.commit()
        cursor.close()
        conn.close()

    def get_user_requests(self) -> list:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_request")
        requests = [UserRequest(
            request_id=row['request_id'],
            user_id=row['user_id'],
            operation=row['operation'],
            timestamp=row['timestamp']
        ) for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return requests