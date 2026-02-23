# Epic Title: Monitor User Behavior Metrics

from sqlalchemy.orm import Session
from backend.analytics.repositories.behavior_metric_repository import BehaviorMetricRepository

class BehaviorMetricService:
    def __init__(self, behavior_metric_repository: BehaviorMetricRepository):
        self.behavior_metric_repository = behavior_metric_repository

    def get_metrics_by_user_id(self, db: Session, user_id: int):
        metrics = self.behavior_metric_repository.get_metrics_by_user_id(user_id)
        avg_session_duration = sum(metric.session_duration for metric in metrics) / len(metrics) if metrics else 0
        total_page_views = sum(metric.page_views for metric in metrics)
        avg_click_through_rate = sum(metric.click_through_rate for metric in metrics) / len(metrics) if metrics else 0
        return {
            "average_session_duration": avg_session_duration,
            "total_page_views": total_page_views,
            "average_click_through_rate": avg_click_through_rate,
            "metrics": metrics
        }

    def create_metric(self, db: Session, user_id: int, session_duration: float, page_views: int, click_through_rate: float) -> dict:
        metric = self.behavior_metric_repository.create_metric(user_id, session_duration, page_views, click_through_rate)
        return {"success": True, "metric": metric}