# Epic Title: Banking Platform — Core API

from backend.models.account import Account
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

    def get_account_by_user_id(self, user_id: int) -> Account:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM account WHERE user_id = %s", (user_id,))
        account_row = cursor.fetchone()
        cursor.close()
        conn.close()
        if account_row:
            return Account(**account_row)
        return None

    def update_account_balance(self, user_id: int, new_balance: float) -> None:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE account SET balance = %s WHERE user_id = %s", (new_balance, user_id))
        conn.commit()
        cursor.close()
        conn.close()