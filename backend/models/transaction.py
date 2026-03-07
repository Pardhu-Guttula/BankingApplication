# Epic Title: Banking Platform — Core API

from datetime import datetime

class Transaction:
    def __init__(self, transaction_id: str, user_id: str, amount: float, timestamp: datetime):
        self.transaction_id = transaction_id
        self.user_id = user_id
        self.amount = amount
        self.timestamp = timestamp