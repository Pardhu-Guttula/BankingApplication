# Epic Title: Banking Platform — Core API

from backend.repositories.header.header_repository import HeaderRepository
from backend.models.header.feature import HeaderFeature

class HeaderService:
    def __init__(self):
        self.repository = HeaderRepository()

    def get_features(self) -> list[HeaderFeature]:
        return self.repository.get_features()

    def add_feature(self, feature_id: str, name: str) -> HeaderFeature:
        feature = HeaderFeature(feature_id, name)
        self.repository.save_feature(feature)
        return feature