# Epic Title: Banking Platform — Core API

class InteractionHistory:
    def __init__(self, interaction_id: int, user_id: int, details: str):
        self.interaction_id = interaction_id
        self.user_id = user_id
        self.details = details