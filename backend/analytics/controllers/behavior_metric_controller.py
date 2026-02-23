# Epic Title: Monitor User Behavior Metrics

from flask import Blueprint, request, jsonify
from sqlalchemy.exc import SQLAlchemyError
from backend.database.config import get_db
from backend.analytics.repositories.behavior_metric_repository import BehaviorMetricRepository
from backend.analytics.services.behavior_metric_service import BehaviorMetricService

behavior_metric_bp = Blueprint('behavior_metric', __name__)

@behavior_metric_bp.route('/behavior_metrics/user/<user_id>', methods=['GET'])
def get_metrics_by_user_id(user_id: int):
    db = next(get_db())

    behavior_metric_repository = BehaviorMetricRepository(db)
    behavior_metric_service = BehaviorMetricService(behavior_metric_repository)

    try:
        result = behavior_metric_service.get_metrics_by_user_id(db, user_id)
        return jsonify(result), 200
    except SQLAlchemyError as e:
        return jsonify({"error": "Unable to process your request"}), 500

@behavior_metric_bp.route('/behavior_metrics/create', methods=['POST'])
def create_metric():
    db = next(get_db())
    data = request.get_json()

    user_id = data.get('user_id')
    session_duration = data.get('session_duration')
    page_views = data.get('page_views')
    click_through_rate = data.get('click_through_rate')

    behavior_metric_repository = BehaviorMetricRepository(db)
    behavior_metric_service = BehaviorMetricService(behavior_metric_repository)

    try:
        result = behavior_metric_service.create_metric(db, user_id, session_duration, page_views, click_through_rate)
        if result['success']:
            metric = result['metric']
            return jsonify({
                "id": metric.id,
                "user_id": metric.user_id,
                "session_duration": metric.session_duration,
                "page_views": metric.page_views,
                "click_through_rate": metric.click_through_rate,
                "created_at": metric.created_at,
                "updated_at": metric.updated_at
            }), 201
        return jsonify({"error": "Metric creation failed"}), 400
    except SQLAlchemyError as e:
        return jsonify({"error": "Unable to process your request"}), 500