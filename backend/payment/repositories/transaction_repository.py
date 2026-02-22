# Epic Title: Integrate payment gateway (Stripe) for processing payments

from backend.payment.models.transaction import Transaction
from typing import Optional
import mysql.connector

class TransactionRepository:
    def __init__(self, db_config: dict):
        self.db_config = db_config
    
    def save_transaction(self, transaction: Transaction) -> bool:
        connection = mysql.connector.connect(**self.db_config)
        cursor = connection.cursor()
        
        try:
            cursor.execute("""
                INSERT INTO transactions (id, amount, currency, status, created_at)
                VALUES (%s, %s, %s, %s, %s)
            """, (transaction.id, transaction.amount, transaction.currency, transaction.status, transaction.created_at))
            connection.commit()
            return True
        finally:
            cursor.close()
            connection.close()
    
    def get_transaction_by_id(self, transaction_id: str) -> Optional[Transaction]:
        connection = mysql.connector.connect(**self.db_config)
        cursor = connection.cursor()
        
        try:
            cursor.execute("""
                SELECT id, amount, currency, status, created_at
                FROM transactions WHERE id = %s
            """, (transaction_id,))
            result = cursor.fetchone()
            if result:
                return Transaction(*result)
            else:
                return None
        finally:
            cursor.close()
            connection.close()