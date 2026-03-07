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

    def get_records_for_deletion(self) -> list[InteractionRecord]:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        query = """
        SELECT interaction_id, user_id, interaction_type, timestamp, location 
        FROM interactions 
        WHERE timestamp < NOW() - INTERVAL %s DAY
        """
        cursor.execute(query, (Settings.RETENTION_PERIOD_DAYS,))
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [InteractionRecord(interaction_id=row[0], user_id=row[1], interaction_type=row[2], timestamp=row[3], location=row[4]) for row in rows]

    def delete_record(self, interaction_id: str) -> None:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM interactions WHERE interaction_id = %s", (interaction_id,))
        conn.commit()
        cursor.close()
        conn.close()

    def get_records_for_compliance(self) -> list[InteractionRecord]:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        query = "SELECT interaction_id, user_id, interaction_type, timestamp, location FROM interactions"
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [InteractionRecord(interaction_id=row[0], user_id=row[1], interaction_type=row[2], timestamp=row[3], location=row[4]) for row in rows]