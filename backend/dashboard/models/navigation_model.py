# Epic Title: Ensure Intuitive Dashboard Interface

class NavigationOption:
    def __init__(self, name: str, link: str):
        self.name = name
        self.link = link

class NavigationModel:
    def __init__(self):
        self.options = [
            NavigationOption('Account Summary', '/dashboard/account_summary'),
            NavigationOption('Transfer Funds', '/dashboard/transfer_funds'),
            NavigationOption('View Statements', '/dashboard/view_statements'),
            NavigationOption('Manage Profile', '/dashboard/manage_profile'),
            NavigationOption('Customer Support', '/dashboard/customer_support')
        ]

    def get_navigation_structure(self) -> list[dict]:
        return [{'name': option.name, 'link': option.link} for option in self.options]