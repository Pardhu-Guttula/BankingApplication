# Epic Title: Banking Platform — Core API

class Log:
    def __init__(self, log_id: str, user_id: str, action: str, timestamp: str, details: str = ''):
        self.log_id = log_id
        self.user_id = user_id
        self.action = action
        self.timestamp = timestamp
        self.details = details