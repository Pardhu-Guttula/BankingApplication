# Epic Title: Banking Platform — Core API

class ModificationRequest:
    def __init__(self, request_id: str, user_id: str, modification_type: str, data: dict):
        self.request_id = request_id
        self.user_id = user_id
        self.modification_type = modification_type
        self.data = data