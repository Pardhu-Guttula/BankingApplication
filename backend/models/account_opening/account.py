# Epic Title: Banking Platform — Core API

class Account:
    def __init__(self, account_id: str, user_id: str, account_type: str, initial_deposit: float):
        self.account_id = account_id
        self.user_id = user_id
        self.account_type = account_type
        self.initial_deposit = initial_deposit