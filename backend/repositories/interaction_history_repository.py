# Epic Title: Banking Platform — Core API

from backend.models.interaction_history import InteractionHistory
import mysql.connector
from mysql.connector import pooling

class InteractionHistoryRepository:
    def __init__(self):
        self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name="mypool",
            pool_size=5,
            host="localhost",
            user="root",
            password="password",
            database="banking"
        )

    def get_interactions_by_user_id(self, user_id: int) -> list:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM interaction_history WHERE user_id = %s", (user_id,))
        interactions = [InteractionHistory(**row) for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return interactions