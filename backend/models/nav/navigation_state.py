# Epic Title: Banking Platform — Core API

class NavigationState:
    def __init__(self, highlighted_link_id: str = None, is_collapsed: bool = False):
        self.highlighted_link_id = highlighted_link_id
        self.is_collapsed = is_collapsed