# Epic Title: Banking Platform — Core API

from backend.models.auth.user import User, AuthToken
import mysql.connector
from mysql.connector import pooling
from datetime import datetime, timedelta

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

    def get_user_by_username(self, username: str) -> User:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row:
            user = User(user_id=row['user_id'], username=row['username'], password_hash=row['password_hash'])
            return user
        return None

    def save_auth_token(self, auth_token: AuthToken) -> None:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO auth_tokens (token, user_id, expires_at) VALUES (%s, %s, %s)",
            (auth_token.token, auth_token.user_id, auth_token.expires_at)
        )
        conn.commit()
        cursor.close()
        conn.close()

    def get_auth_token(self, token: str) -> AuthToken:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM auth_tokens WHERE token = %s", (token,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row:
            auth_token = AuthToken(token=row['token'], user_id=row['user_id'], expires_at=row['expires_at'])
            return auth_token
        return None

    def remove_auth_token(self, token: str) -> None:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM auth_tokens WHERE token = %s", (token,))
        conn.commit()
        cursor.close()
        conn.close()

    def remove_expired_tokens(self) -> None:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM auth_tokens WHERE expires_at < %s", (datetime.now(),))
        conn.commit()
        cursor.close()
        conn.close()