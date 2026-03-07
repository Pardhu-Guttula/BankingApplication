# Epic Title: Banking Platform — Core API

class MonitoringDashboard:
    def __init__(self, alerts: List[str], performance_reports: List[str]):
        self.alerts = alerts
        self.performance_reports = performance_reports

    def add_alert(self, alert: str):
        self.alerts.append(alert)

    def add_performance_report(self, report: str):
        self.performance_reports.append(report)

    def get_alerts(self) -> List[str]:
        return self.alerts

    def get_performance_reports(self) -> List[str]:
        return self.performance_reports