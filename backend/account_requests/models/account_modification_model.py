# Epic Title: User-Friendly Account Service Interface

class AccountModificationOption:
    def __init__(self, name: str, link: str):
        self.name = name
        self.link = link

class AccountModificationNavigation:
    def __init__(self):
        self.sections = [
            {
                'name': 'Manage Services',
                'actions': [
                    AccountModificationOption('Update Account Details', '/account/update_details'),
                    AccountModificationOption('Request Account Closure', '/account/request_closure')
                ]
            },
            {
                'name': 'Modify Preferences',
                'actions': [
                    AccountModificationOption('Change Notification Settings', '/account/change_notifications'),
                    AccountModificationOption('Update Security Settings', '/account/update_security')
                ]
            },
            {
                'name': 'Account History',
                'actions': [
                    AccountModificationOption('View Transaction History', '/account/transaction_history'),
                    AccountModificationOption('Download Statements', '/account/download_statements')
                ]
            }
        ]

    def get_navigation_structure(self) -> dict:
        return {
            'sections': [
                {
                    'name': section['name'],
                    'actions': [{'name': action.name, 'link': action.link} for action in section['actions']]
                } for section in self.sections
            ]
        }