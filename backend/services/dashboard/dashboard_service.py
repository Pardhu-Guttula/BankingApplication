# Epic Title: Banking Platform — Core API

from backend.repositories.dashboard.dashboard_repository import DashboardRepository
from backend.models.dashboard.dashboard import Dashboard

class DashboardService:
    def __init__(self):
        self.repository = DashboardRepository()

    def get_dashboard(self, dashboard_id: str) -> Dashboard:
        return self.repository.get_dashboard(dashboard_id)

    def add_dashboard(self, dashboard_id: str, name: str) -> Dashboard:
        dashboard = Dashboard(dashboard_id, name)
        self.repository.save_dashboard(dashboard)
        return dashboard