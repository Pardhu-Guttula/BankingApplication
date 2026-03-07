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

    def get_interactions(self, user_id: str, date_start: str = None, date_end: str = None) -> list[InteractionRecord]:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        query = "SELECT interaction_id, user_id, interaction_type, timestamp FROM interactions WHERE user_id = %s"
        params = [user_id]
        if date_start and date_end:
            query += " AND timestamp BETWEEN %s AND %s"
            params.extend([date_start, date_end])
        cursor.execute(query, tuple(params))
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [InteractionRecord(interaction_id=row[0], user_id=row[1], interaction_type=row[2], timestamp=row[3]) for row in rows]