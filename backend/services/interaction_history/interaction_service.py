# Epic Title: Banking Platform — Core API

from backend.repositories.interaction_history.interaction_repository import InteractionRepository
from backend.models.interaction_history.interaction_record import InteractionRecord

class InteractionService:
    def __init__(self):
        self.repository = InteractionRepository()

    def search_interactions(self, event_type: str) -> list[InteractionRecord]:
        return self.repository.search_interactions(event_type)