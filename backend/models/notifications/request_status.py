# Epic Title: Banking Platform — Core API

class RequestStatus:
    def __init__(self, request_id: str, status: str):
        self.request_id = request_id
        self.status = status