# Epic Title: Banking Platform — Core API

from backend.models.dashboard.banking_product import BankingProduct
import mysql.connector
from mysql.connector import pooling

class BankingProductRepository:
    def __init__(self):
        self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name="mypool",
            pool_size=5,
            host="localhost",
            user="root",
            password="password",
            database="banking"
        )

    def save_banking_product(self, product: BankingProduct) -> None:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO banking_product (product_id, name, description, eligibility_criteria) VALUES (%s, %s, %s, %s)",
            (product.product_id, product.name, product.description, product.eligibility_criteria)
        )
        conn.commit()
        cursor.close()
        conn.close()

    def get_all_banking_products(self) -> list:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM banking_product")
        products = [BankingProduct(
            product_id=row['product_id'],
            name=row['name'],
            description=row['description'],
            eligibility_criteria=row['eligibility_criteria']
        ) for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return products

    def get_eligible_products(self, eligibility_criteria: str) -> list:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM banking_product WHERE eligibility_criteria = %s", (eligibility_criteria,))
        products = [BankingProduct(
            product_id=row['product_id'],
            name=row['name'],
            description=row['description'],
            eligibility_criteria=row['eligibility_criteria']
        ) for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return products

    def get_product_details(self, product_id: str) -> BankingProduct:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM banking_product WHERE product_id = %s", (product_id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row:
            product = BankingProduct(
                product_id=row['product_id'],
                name=row['name'],
                description=row['description'],
                eligibility_criteria=row['eligibility_criteria']
            )
            return product
        return None