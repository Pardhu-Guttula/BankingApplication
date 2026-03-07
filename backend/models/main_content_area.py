# Epic Title: Banking Platform — Core API

from typing import List

class MainContentView:
    def __init__(self, name: str, content: str):
        self.name = name
        self.content = content

class MainContentArea:
    def __init__(self, views: List[MainContentView]):
        self.views = views
        self.current_view = None if not views else views[0]

    def add_view(self, view: MainContentView):
        self.views.append(view)

    def remove_view(self, view: MainContentView):
        self.views.remove(view)

    def get_views(self) -> List[MainContentView]:
        return self.views

    def set_current_view(self, view: MainContentView):
        if view in self.views:
            self.current_view = view

    def get_current_view(self) -> MainContentView:
        return self.current_view