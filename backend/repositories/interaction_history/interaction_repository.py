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

    def get_interactions(self, interaction_type: str) -> list[InteractionRecord]:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT interaction_id, user_id, interaction_type, timestamp FROM interactions WHERE interaction_type = %s", (interaction_type,))
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [InteractionRecord(interaction_id=row[0], user_id=row[1], interaction_type=row[2], timestamp=row[3]) for row in rows]

    def save_interaction(self, interaction: InteractionRecord) -> None:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO interactions (interaction_id, user_id, interaction_type, timestamp) VALUES (%s, %s, %s, %s)",
            (interaction.interaction_id, interaction.user_id, interaction.interaction_type, interaction.timestamp)
        )
        conn.commit()
        cursor.close()
        conn.close()