# Epic Title: Banking Platform — Core API

from backend.models.account_opening.account import Account
import mysql.connector
from mysql.connector import pooling

class AccountRepository:
    def __init__(self):
        self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name="mypool",
            pool_size=5,
            host="localhost",
            user="root",
            password="password",
            database="banking"
        )

    def save_account(self, account: Account) -> None:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO accounts (account_id, user_id, account_type, initial_deposit) VALUES (%s, %s, %s, %s)",
            (account.account_id, account.user_id, account.account_type, account.initial_deposit)
        )
        conn.commit()
        cursor.close()
        conn.close()