# Epic Title: Banking Platform — Core API

from backend.models.browser import Browser
import mysql.connector
from mysql.connector import pooling

class BrowserRepository:
    def __init__(self):
        self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name="mypool",
            pool_size=5,
            host="localhost",
            user="root",
            password="password",
            database="banking"
        )

    def save_browser(self, browser: Browser) -> None:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO browser (name, version) VALUES (%s, %s)",
            (browser.name, browser.version)
        )
        conn.commit()
        cursor.close()
        conn.close()

    def get_browsers(self) -> list:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM browser")
        browsers = [Browser(
            name=row['name'],
            version=row['version']
        ) for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return browsers