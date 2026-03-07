# Epic Title: Banking Platform — Core API

from backend.repositories.database.transaction_repository import TransactionRepository
from backend.models.transaction import Transaction
from datetime import datetime

class TransactionService:
    def __init__(self):
        self.repository = TransactionRepository()

    def create_transaction(self, transaction_id: str, user_id: str, amount: float):
        timestamp = datetime.now()
        transaction = Transaction(transaction_id, user_id, amount, timestamp)
        self.repository.save_transaction(transaction)
        return transaction

    def get_all_transactions(self) -> list:
        return self.repository.get_transactions()