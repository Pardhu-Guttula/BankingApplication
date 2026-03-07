# Epic Title: Banking Platform — Core API

from backend.repositories.interaction_history.interaction_repository import InteractionRepository
from backend.models.interaction_history.interaction_record import InteractionRecord

class InteractionService:
    def __init__(self):
        self.repository = InteractionRepository()

    def get_interactions(self, user_id: str, interaction_type: str = None) -> list[InteractionRecord]:
        return self.repository.get_interactions(user_id, interaction_type)