# Epic Title: Ensure Intuitive Dashboard Interface

from backend.dashboard.models.dashboard_navigation_model import DashboardNavigation

class DashboardNavigationService:

    @staticmethod
    def get_dashboard_navigation() -> dict:
        navigation = DashboardNavigation()
        return navigation.get_navigation_structure()