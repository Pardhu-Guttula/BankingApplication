# Epic Title: Banking Platform — Core API

import mysql.connector
from mysql.connector import pooling
from backend.models.header.feature import HeaderFeature

class HeaderRepository:
    def __init__(self):
        self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name="mypool",
            pool_size=5,
            host="localhost",
            user="root",
            password="password",
            database="banking"
        )

    def get_features(self) -> list[HeaderFeature]:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT feature_id, name FROM header_features")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [HeaderFeature(feature_id=row[0], name=row[1]) for row in rows]

    def save_feature(self, feature: HeaderFeature) -> None:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO header_features (feature_id, name) VALUES (%s, %s)",
            (feature.feature_id, feature.name)
        )
        conn.commit()
        cursor.close()
        conn.close()