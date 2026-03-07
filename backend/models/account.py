# Epic Title: Banking Platform — Core API

class Account:
    def __init__(self, account_id: int, user_id: int, balance: float):
        self.account_id = account_id
        self.user_id = user_id
        self.balance = balance