# Epic Title: Banking Platform — Core API

from backend.services.interaction_history.data_retention_service import DataRetentionService

def data_retention_middleware(func):
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        retention_service = DataRetentionService()
        retention_service.notify_before_deletion()
        return response
    return wrapper