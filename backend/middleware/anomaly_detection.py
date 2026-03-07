# Epic Title: Banking Platform — Core API

from backend.services.interaction_history.anomaly_detection_service import AnomalyDetectionService

def anomaly_detection_middleware(func):
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        anomaly_service = AnomalyDetectionService()
        anomaly_service.detect_anomalies()
        return response
    return wrapper