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

    def search_interactions(self, event_type: str) -> list[InteractionRecord]:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        query = "SELECT interaction_id, user_id, interaction_type, timestamp, location FROM interactions WHERE interaction_type = %s"
        cursor.execute(query, (event_type,))
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [InteractionRecord(interaction_id=row[0], user_id=row[1], interaction_type=row[2], timestamp=row[3], location=row[4]) for row in rows]