# Epic Title: Ensure Intuitive Dashboard Interface

class NavigationSection:
    def __init__(self, name: str, actions: list):
        self.name = name
        self.actions = actions

class DashboardNavigation:
    def __init__(self):
        self.sections = [
            NavigationSection(
                name='Overview',
                actions=[
                    {'name': 'View Account Balance', 'link': '/dashboard/account_balance'},
                    {'name': 'Recent Transactions', 'link': '/dashboard/recent_transactions'}
                ]
            ),
            NavigationSection(
                name='Manage Accounts',
                actions=[
                    {'name': 'Open New Account', 'link': '/dashboard/open_account'},
                    {'name': 'Close Account', 'link': '/dashboard/close_account'}
                ]
            ),
            NavigationSection(
                name='Settings',
                actions=[
                    {'name': 'Profile Settings', 'link': '/dashboard/profile_settings'},
                    {'name': 'Security Settings', 'link': '/dashboard/security_settings'}
                ]
            )
        ]

    def get_navigation_structure(self) -> dict:
        return {
            'sections': [
                {
                    'name': section.name,
                    'actions': section.actions
                } for section in self.sections
            ]
        }