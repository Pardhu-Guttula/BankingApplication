# Epic Title: Banking Platform — Core API

class RequestForm:
    def __init__(self, user_id: str, account_type: str, initial_deposit: float):
        self.user_id = user_id
        self.account_type = account_type
        self.initial_deposit = initial_deposit