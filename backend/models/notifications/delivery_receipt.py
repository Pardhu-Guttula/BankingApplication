# Epic Title: Banking Platform — Core API

class DeliveryReceipt:
    def __init__(self, receipt_id: str, email: str, status: str):
        self.receipt_id = receipt_id
        self.email = email
        self.status = status