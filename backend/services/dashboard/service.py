# Epic Title: Banking Platform — Core API

from backend.repositories.dashboard.service_repository import ServiceRepository
from backend.models.dashboard.service import BankingService

class Service:
    def __init__(self):
        self.repository = ServiceRepository()

    def add_banking_service(self, service_id: str, name: str, description: str, eligibility_criteria: str):
        service = BankingService(service_id, name, description, eligibility_criteria)
        self.repository.save_banking_service(service)
        return service

    def get_all_services(self) -> list:
        return self.repository.get_all_banking_services()

    def get_eligible_services(self, eligibility_criteria: str) -> list:
        return self.repository.get_eligible_services(eligibility_criteria)

    def get_service_details(self, service_id: str) -> BankingService:
        return self.repository.get_service_details(service_id)