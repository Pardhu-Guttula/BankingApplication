# Epic Title: Banking Platform — Core API

from backend.repositories.interaction_history.interaction_repository import InteractionRepository
from backend.models.interaction_history.interaction_record import InteractionRecord
import uuid
from datetime import datetime

class InteractionService:
    def __init__(self):
        self.repository = InteractionRepository()

    def track_login(self, user_id: str) -> InteractionRecord:
        interaction = InteractionRecord(
            interaction_id=str(uuid.uuid4()),
            user_id=user_id,
            interaction_type="login",
            timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        )
        self.repository.save_interaction(interaction)
        return interaction

    def track_page_visit(self, user_id: str, location: str) -> InteractionRecord:
        interaction = InteractionRecord(
            interaction_id=str(uuid.uuid4()),
            user_id=user_id,
            interaction_type="page_visit",
            timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            location=location
        )
        self.repository.save_interaction(interaction)
        return interaction

    def track_form_submission(self, user_id: str, location: str) -> InteractionRecord:
        interaction = InteractionRecord(
            interaction_id=str(uuid.uuid4()),
            user_id=user_id,
            interaction_type="form_submission",
            timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            location=location
        )
        self.repository.save_interaction(interaction)
        return interaction

    def get_interactions(self, user_id: str) -> list[InteractionRecord]:
        return self.repository.get_interactions(user_id)