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

    def get_failed_logins(self) -> list[InteractionRecord]:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT interaction_id, user_id, interaction_type, timestamp, location FROM interactions WHERE interaction_type = 'failed_login'")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [InteractionRecord(interaction_id=row[0], user_id=row[1], interaction_type=row[2], timestamp=row[3], location=row[4]) for row in rows]

    def get_unusual_locations(self) -> list[InteractionRecord]:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT interaction_id, user_id, interaction_type, timestamp, location FROM interactions WHERE location = 'unusual'")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [InteractionRecord(interaction_id=row[0], user_id=row[1], interaction_type=row[2], timestamp=row[3], location=row[4]) for row in rows]

    def get_repeated_exports(self) -> list[InteractionRecord]:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT interaction_id, user_id, interaction_type, timestamp, location FROM interactions WHERE interaction_type = 'data_export' AND timestamp >= NOW() - INTERVAL 1 MINUTE")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [InteractionRecord(interaction_id=row[0], user_id=row[1], interaction_type=row[2], timestamp=row[3], location=row[4]) for row in rows]