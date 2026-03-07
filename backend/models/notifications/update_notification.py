# Epic Title: Banking Platform — Core API

class UpdateNotification:
    def __init__(self, request_id: str, status: str, message: str):
        self.request_id = request_id
        self.status = status
        self.message = message