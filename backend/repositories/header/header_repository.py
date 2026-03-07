# Epic Title: Banking Platform — Core API

import mysql.connector
from mysql.connector import pooling
from backend.models.header.header_element import HeaderElement

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

    def get_header_elements(self) -> list[HeaderElement]:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT element_id, content FROM header_elements")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [HeaderElement(element_id=row[0], content=row[1]) for row in rows]

    def save_header_element(self, header_element: HeaderElement) -> None:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO header_elements (element_id, content) VALUES (%s, %s)",
            (header_element.element_id, header_element.content)
        )
        conn.commit()
        cursor.close()
        conn.close()