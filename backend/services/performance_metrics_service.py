# Epic Title: Banking Platform — Core API

from backend.repositories.database.performance_metrics_repository import PerformanceMetricsRepository
from backend.models.performance_metrics import PerformanceMetrics
from datetime import datetime

class PerformanceMetricsService:
    def __init__(self):
        self.repository = PerformanceMetricsRepository()

    def log_metrics(self, metrics_id: str, operation: str, duration: float):
        timestamp = datetime.now()
        metrics = PerformanceMetrics(metrics_id, operation, duration, timestamp)
        self.repository.save_performance_metrics(metrics)
        return metrics

    def get_all_metrics(self) -> list:
        return self.repository.get_performance_metrics()