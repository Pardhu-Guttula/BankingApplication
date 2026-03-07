# Epic Title: Banking Platform — Core API

import mysql.connector
from mysql.connector import pooling
from backend.models.interaction_history.interaction_record import InteractionRecord
from backend.config.settings import Settings

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

    def get_interactions(self, user_id: str) -> list[InteractionRecord]:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT interaction_id, user_id, interaction_type, timestamp, location FROM interactions WHERE user_id = %s", (user_id,))
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        interactions = [InteractionRecord(interaction_id=row[0], user_id=row[1], interaction_type=row[2], timestamp=row[3], location=row[4]).decrypt_data(Settings.ENCRYPTION_KEY) for row in rows]
        return interactions

    def save_interaction(self, interaction: InteractionRecord) -> None:
        encrypted_interaction = interaction.encrypt_data(Settings.ENCRYPTION_KEY)
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO interactions (interaction_id, user_id, interaction_type, timestamp, location) VALUES (%s, %s, %s, %s, %s)",
            (encrypted_interaction.interaction_id, encrypted_interaction.user_id, encrypted_interaction.interaction_type, encrypted_interaction.timestamp, encrypted_interaction.location)
        )
        conn.commit()
        cursor.close()
        conn.close()

    def get_anonymized_interactions(self) -> list[InteractionRecord]:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT interaction_id, interaction_type, timestamp, location FROM interactions")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        interactions = [InteractionRecord(interaction_id=row[0], user_id="ANONYMOUS", interaction_type=row[1], timestamp=row[2], location=row[3]) for row in rows]
        return interactions