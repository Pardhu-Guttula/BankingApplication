# Epic Title: Banking Platform — Core API

from backend.repositories.database.monitoring_repository import MonitoringRepository

class MonitoringService:
    def __init__(self):
        self.repository = MonitoringRepository()

    def generate_alert(self, alert: str):
        self.repository.save_alert(alert)

    def generate_performance_report(self, report: str):
        self.repository.save_performance_report(report)

    def get_all_alerts(self) -> list:
        return self.repository.get_alerts()

    def get_all_performance_reports(self) -> list:
        return self.repository.get_performance_reports()