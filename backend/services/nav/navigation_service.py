# Epic Title: Banking Platform — Core API

from backend.repositories.nav.navigation_repository import NavigationRepository
from backend.models.nav.navigation_state import NavigationState

class NavigationService:
    def __init__(self):
        self.repository = NavigationRepository()

    def get_navigation_links(self) -> list[NavigationLink]:
        return self.repository.get_navigation_links()

    def update_navigation_state(self, highlighted_link_id: str, is_collapsed: bool) -> NavigationState:
        state = NavigationState(highlighted_link_id, is_collapsed)
        return state