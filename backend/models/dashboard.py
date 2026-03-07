# Epic Title: Banking Platform — Core API

class Dashboard:
    def __init__(self, user_id: int):
        self.user_id = user_id
        self.widgets = []

    def add_widget(self, widget: object):
        self.widgets.append(widget)

    def remove_widget(self, widget: object):
        self.widgets.remove(widget)

    def get_widgets(self) -> list:
        return self.widgets