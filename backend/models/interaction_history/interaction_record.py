# Epic Title: Banking Platform — Core API

class InteractionRecord:
    def __init__(self, interaction_id: str, user_id: str, interaction_type: str, timestamp: str, location: str = ''):
        self.interaction_id = interaction_id
        self.user_id = user_id
        self.interaction_type = interaction_type
        self.timestamp = timestamp
        self.location = location