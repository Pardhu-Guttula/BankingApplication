# Epic Title: Banking Platform — Core API

from backend.repositories.dashboard_repository import DashboardRepository
from backend.models.main_content_area import MainContentArea
from backend.models.side_navigation import SideNavigation
from backend.models.header import Header
from backend.models.dashboard import Dashboard

class DashboardService:
    def __init__(self, repository: DashboardRepository):
        self.repository = repository

    def create_dashboard(self, main_content: MainContentArea, side_navigation: SideNavigation, header: Header):
        dashboard = Dashboard(main_content, side_navigation, header)
        self.repository.save_dashboard(dashboard)
        return dashboard

    def get_dashboard(self) -> Dashboard:
        return self.repository.load_dashboard()