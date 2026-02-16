# Epic Title: User-Friendly Account Service Interface

from backend.account_requests.models.account_modification_model import AccountModificationNavigation

class AccountModificationService:

    @staticmethod
    def get_modification_navigation() -> dict:
        navigation = AccountModificationNavigation()
        return navigation.get_navigation_structure()