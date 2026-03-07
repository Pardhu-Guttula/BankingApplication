# Epic Title: Banking Platform — Core API

class ServiceRequest:
    def __init__(self, request_id: int, user_id: int, description: str, status: str):
        self.request_id = request_id
        self.user_id = user_id
        self.description = description
        self.status = status