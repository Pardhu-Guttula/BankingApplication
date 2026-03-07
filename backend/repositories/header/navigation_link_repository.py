# Epic Title: Banking Platform — Core API

import mysql.connector
from mysql.connector import pooling
from backend.models.header.navigation_link import NavigationLink

class NavigationLinkRepository:
    def __init__(self):
        self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name="mypool",
            pool_size=5,
            host="localhost",
            user="root",
            password="password",
            database="banking"
        )

    def get_all_links(self) -> list[NavigationLink]:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT link_id, name, route, key_functionality FROM navigation_links")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [NavigationLink(link_id=row[0], name=row[1], route=row[2], key_functionality=row[3]) for row in rows]

    def update_link(self, navigation_link: NavigationLink) -> None:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE navigation_links SET name = %s, route = %s, key_functionality = %s WHERE link_id = %s",
                       (navigation_link.name, navigation_link.route, navigation_link.key_functionality, navigation_link.link_id))
        conn.commit()
        cursor.close()
        conn.close()