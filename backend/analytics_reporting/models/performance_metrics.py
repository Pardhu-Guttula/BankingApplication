# Epic Title: Generate detailed e-commerce performance reports

from dataclasses import dataclass
import datetime

@dataclass
class PerformanceMetrics:
    metric_id: int
    date: datetime.date
    sales_quantity: int
    total_revenue: float
    avg_session_duration: float
    total_page_views: int
    click_through_rate: float