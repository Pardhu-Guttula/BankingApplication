# Epic Title: Banking Platform — Core API

from backend.models.dashboard.service import BankingService
import mysql.connector
from mysql.connector import pooling

class ServiceRepository:
    def __init__(self):
        self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name="mypool",
            pool_size=5,
            host="localhost",
            user="root",
            password="password",
            database="banking"
        )

    def save_banking_service(self, service: BankingService) -> None:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO banking_service (service_id, name, description, eligibility_criteria) VALUES (%s, %s, %s, %s)",
            (service.service_id, service.name, service.description, service.eligibility_criteria)
        )
        conn.commit()
        cursor.close()
        conn.close()

    def get_all_banking_services(self) -> list:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM banking_service")
        services = [BankingService(
            service_id=row['service_id'],
            name=row['name'],
            description=row['description'],
            eligibility_criteria=row['eligibility_criteria']
        ) for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return services

    def get_eligible_services(self, eligibility_criteria: str) -> list:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM banking_service WHERE eligibility_criteria = %s", (eligibility_criteria,))
        services = [BankingService(
            service_id=row['service_id'],
            name=row['name'],
            description=row['description'],
            eligibility_criteria=row['eligibility_criteria']
        ) for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return services

    def get_service_details(self, service_id: str) -> BankingService:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM banking_service WHERE service_id = %s", (service_id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row:
            service = BankingService(
                service_id=row['service_id'],
                name=row['name'],
                description=row['description'],
                eligibility_criteria=row['eligibility_criteria']
            )
            return service
        return None