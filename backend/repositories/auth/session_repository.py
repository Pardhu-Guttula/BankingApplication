# Epic Title: Banking Platform — Core API

from backend.models.auth.user_session import UserSession, AuthToken
import mysql.connector
from mysql.connector import pooling
from datetime import datetime

class SessionRepository:
    def __init__(self):
        self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name="mypool",
            pool_size=5,
            host="localhost",
            user="root",
            password="password",
            database="banking"
        )

    def save_user_session(self, user_session: UserSession):
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO user_sessions (session_id, user_id, expires_at) VALUES (%s, %s, %s)",
            (user_session.session_id, user_session.user_id, user_session.expires_at)
        )
        conn.commit()
        cursor.close()
        conn.close()

    def get_user_session(self, session_id: str) -> UserSession:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_sessions WHERE session_id = %s", (session_id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row:
            user_session = UserSession(
                session_id=row['session_id'],
                user_id=row['user_id'],
                expires_at=row['expires_at']
            )
            return user_session
        return None

    def save_auth_token(self, auth_token: AuthToken):
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
            auth_token = AuthToken(
                token=row['token'],
                user_id=row['user_id'],
                expires_at=row['expires_at']
            )
            return auth_token
        return None

    def remove_auth_token(self, token: str):
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM auth_tokens WHERE token = %s", (token,))
        conn.commit()
        cursor.close()
        conn.close()

    def remove_expired_tokens(self):
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM auth_tokens WHERE expires_at < %s", (datetime.now(),))
        conn.commit()
        cursor.close()
        conn.close()

    def remove_expired_sessions(self):
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM user_sessions WHERE expires_at < %s", (datetime.now(),))
        conn.commit()
        cursor.close()
        conn.close()