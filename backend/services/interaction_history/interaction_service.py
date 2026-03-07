# Epic Title: Banking Platform — Core API

from backend.repositories.interaction_history.interaction_repository import InteractionRepository
from backend.models.interaction_history.interaction_record import InteractionRecord

class InteractionService:
    def __init__(self):
        self.repository = InteractionRepository()

    def get_interactions(self, user_id: str) -> list[InteractionRecord]:
        return self.repository.get_interactions(user_id)

    def add_interaction(self, interaction_id: str, user_id: str, interaction_type: str, timestamp: str, location: str) -> InteractionRecord:
        interaction = InteractionRecord(interaction_id, user_id, interaction_type, timestamp, location)
        self.repository.save_interaction(interaction)
        return interaction

    def get_anonymized_interactions(self) -> list[InteractionRecord]:
        return self.repository.get_anonymized_interactions()

    def verify_access_control(self, user_id: str, requested_user_id: str) -> bool:
        return user_id == requested_user_id