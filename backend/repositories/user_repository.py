# Epic Title: Banking Platform — Core API

from backend.models.user import User
import mysql.connector
from mysql.connector import pooling

class UserRepository:
    def __init__(self):
        self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name="mypool",
            pool_size=5,
            host="localhost",
            user="root",
            password="password",
            database="banking"
        )

    def get_user_by_id(self, user_id: int) -> User:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user WHERE user_id = %s", (user_id,))
        user_row = cursor.fetchone()
        cursor.close()
        conn.close()
        if user_row:
            return User(**user_row)
        return None

    def get_user_by_username(self, username: str) -> User:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user WHERE username = %s", (username,))
        user_row = cursor.fetchone()
        cursor.close()
        conn.close()
        if user_row:
            return User(**user_row)
        return None