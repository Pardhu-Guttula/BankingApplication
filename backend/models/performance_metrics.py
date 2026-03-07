# Epic Title: Banking Platform — Core API

from datetime import datetime

class PerformanceMetrics:
    def __init__(self, metrics_id: str, operation: str, duration: float, timestamp: datetime):
        self.metrics_id = metrics_id
        self.operation = operation
        self.duration = duration
        self.timestamp = timestamp