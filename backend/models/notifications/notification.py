# Epic Title: Banking Platform — Core API

class Notification:
    def __init__(self, user_id: str, notification_type: str, message: str, timestamp: str):
        self.user_id = user_id
        self.notification_type = notification_type
        self.message = message
        self.timestamp = timestamp