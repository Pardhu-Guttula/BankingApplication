# Epic Title: Banking Platform — Core API

import mysql.connector
from mysql.connector import pooling
from backend.models.nav.navigation_link import NavigationLink

class NavigationRepository:
    def __init__(self):
        self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name="mypool",
            pool_size=5,
            host="localhost",
            user="root",
            password="password",
            database="banking"
        )

    def get_navigation_links(self) -> list[NavigationLink]:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT link_id, title, url FROM navigation_links")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [NavigationLink(link_id=row[0], title=row[1], url=row[2]) for row in rows]