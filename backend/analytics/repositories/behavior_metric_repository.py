# Epic Title: Monitor User Behavior Metrics

from sqlalchemy.orm import Session
from backend.analytics.models.behavior_metric import BehaviorMetric

class BehaviorMetricRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_metrics_by_user_id(self, user_id: int) -> list:
        return self.db.query(BehaviorMetric).filter(BehaviorMetric.user_id == user_id).all()

    def create_metric(self, user_id: int, session_duration: float, page_views: int, click_through_rate: float) -> BehaviorMetric:
        metric = BehaviorMetric(
            user_id=user_id,
            session_duration=session_duration,
            page_views=page_views,
            click_through_rate=click_through_rate
        )
        self.db.add(metric)
        self.db.commit()
        self.db.refresh(metric)
        return metric