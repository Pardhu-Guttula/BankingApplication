# Epic Title: Ensure Intuitive Dashboard Interface

from backend.dashboard.models.navigation_model import NavigationModel

class NavigationService:

    @staticmethod
    def get_navigation_options() -> list[dict]:
        navigation_model = NavigationModel()
        return navigation_model.get_navigation_structure()