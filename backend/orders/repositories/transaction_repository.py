# Epic Title: Display Order Confirmation to Customers After Successful Payment

from sqlalchemy.orm import Session
from backend.payment.models.transaction import Transaction

class TransactionRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_transaction_by_id(self, transaction_id: str) -> Transaction:
        return self.db.query(Transaction).filter(Transaction.transaction_id == transaction_id).first()