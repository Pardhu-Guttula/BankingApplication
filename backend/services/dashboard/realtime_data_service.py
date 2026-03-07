# Epic Title: Banking Platform — Core API

from backend.repositories.dashboard.realtime_data_repository import RealTimeDataRepository
from backend.models.dashboard.dashboard import RealTimeData
from datetime import datetime

class RealTimeDataService:
    def __init__(self):
        self.repository = RealTimeDataRepository()

    def update_realtime_data(self, data_id: str, content: str):
        timestamp = datetime.now()
        realtime_data = RealTimeData(data_id, content, timestamp)
        self.repository.save_realtime_data(realtime_data)
        return realtime_data

    def get_latest_data(self) -> RealTimeData:
        return self.repository.get_latest_data()