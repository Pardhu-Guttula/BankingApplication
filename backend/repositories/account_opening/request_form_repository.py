# Epic Title: Banking Platform — Core API

from backend.models.account_opening.request_form import RequestForm
import mysql.connector
from mysql.connector import pooling

class RequestFormRepository:
    def __init__(self):
        self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name="mypool",
            pool_size=5,
            host="localhost",
            user="root",
            password="password",
            database="banking"
        )

    def save_request_form(self, request_form: RequestForm) -> None:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO request_forms (user_id, account_type, initial_deposit) VALUES (%s, %s, %s)",
            (request_form.user_id, request_form.account_type, request_form.initial_deposit)
        )
        conn.commit()
        cursor.close()
        conn.close()