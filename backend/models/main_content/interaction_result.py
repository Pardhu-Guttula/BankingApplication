# Epic Title: Banking Platform — Core API

class InteractionResult:
    def __init__(self, success: bool, message: str):
        self.success = success
        self.message = message