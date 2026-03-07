# Epic Title: Banking Platform — Core API

class NavigationLink:
    def __init__(self, link_id: str, name: str, route: str, key_functionality: bool = False):
        self.link_id = link_id
        self.name = name
        self.route = route
        self.key_functionality = key_functionality