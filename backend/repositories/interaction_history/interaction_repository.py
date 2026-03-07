# Epic Title: Banking Platform — Core API

import mysql.connector
from mysql.connector import pooling
from backend.models.interaction_history.interaction_record import InteractionRecord

class InteractionRepository:
    def __init__(self):
        self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name="mypool",
            pool_size=5,
            host="localhost",
            user="root",
            password="password",
            database="banking"
        )

    def get_interactions(self, user_id: str, interaction_type: str = None) -> list[InteractionRecord]:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        query = "SELECT interaction_id, user_id, interaction_type, timestamp, location FROM interactions WHERE user_id = %s"
        params = [user_id]
        if interaction_type:
            query += " AND interaction_type = %s"
            params.append(interaction_type)
        cursor.execute(query, tuple(params))
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [InteractionRecord(interaction_id=row[0], user_id=row[1], interaction_type=row[2], timestamp=row[3], location=row[4]) for row in rows]