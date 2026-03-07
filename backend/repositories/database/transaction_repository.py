# Epic Title: Banking Platform — Core API

from backend.models.transaction import Transaction
import mysql.connector
from mysql.connector import pooling
from datetime import datetime

class TransactionRepository:
    def __init__(self):
        self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name="mypool",
            pool_size=5,
            host="localhost",
            user="root",
            password="password",
            database="banking"
        )

    def save_transaction(self, transaction: Transaction) -> None:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO transaction (transaction_id, user_id, amount, timestamp) VALUES (%s, %s, %s, %s)",
            (transaction.transaction_id, transaction.user_id, transaction.amount, transaction.timestamp)
        )
        conn.commit()
        cursor.close()
        conn.close()

    def get_transactions(self) -> list:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM transaction")
        transactions = [Transaction(
            transaction_id=row['transaction_id'],
            user_id=row['user_id'],
            amount=row['amount'],
            timestamp=row['timestamp']
        ) for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return transactions