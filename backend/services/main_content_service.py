# Epic Title: Banking Platform — Core API

from backend.repositories.main_content_repository import MainContentRepository
from backend.models.main_content_area import MainContentArea, MainContentView

class MainContentService:
    def __init__(self, repository: MainContentRepository):
        self.repository = repository

    def create_main_content_area(self, views: list):
        view_objects = [MainContentView(
            name=view["name"],
            content=view["content"]
        ) for view in views]

        main_content_area = MainContentArea(views=view_objects)
        self.repository.save_main_content_area(main_content_area)

    def get_main_content_area(self) -> MainContentArea:
        return self.repository.get_main_content_area()