# Epic Title: Banking Platform — Core API

class RealTimeData:
    def __init__(self, data_id: str, content: str, timestamp: datetime):
        self.data_id = data_id
        self.content = content
        self.timestamp = timestamp