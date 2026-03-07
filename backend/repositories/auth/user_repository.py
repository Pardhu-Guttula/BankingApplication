# Epic Title: Banking Platform — Core API

import mysql.connector
from mysql.connector import pooling
from backend.models.auth.user import User

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

    def get_user(self, user_id: str) -> User:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT user_id, username FROM users WHERE user_id = %s", (user_id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        roles = self.get_user_roles(user_id)
        return User(user_id=row[0], username=row[1], roles=roles)

    def get_user_roles(self, user_id: str) -> list[str]:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT role_name FROM user_roles WHERE user_id = %s", (user_id,))
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [row[0] for row in rows]

    def assign_role(self, user_id: str, role_name: str) -> None:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO user_roles (user_id, role_name) VALUES (%s, %s)", (user_id, role_name))
        conn.commit()
        cursor.close()
        conn.close()

    def revoke_role(self, user_id: str, role_name: str) -> None:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM user_roles WHERE user_id = %s AND role_name = %s", (user_id, role_name))
        conn.commit()
        cursor.close()
        conn.close()