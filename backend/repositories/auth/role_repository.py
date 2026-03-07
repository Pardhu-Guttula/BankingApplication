# Epic Title: Banking Platform — Core API

import mysql.connector
from mysql.connector import pooling
from backend.models.auth.role import Role

class RoleRepository:
    def __init__(self):
        self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name="mypool",
            pool_size=5,
            host="localhost",
            user="root",
            password="password",
            database="banking"
        )

    def create_role(self, role: Role) -> None:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO roles (role_id, role_name) VALUES (%s, %s)", (role.role_id, role.role_name))
        conn.commit()
        cursor.close()
        conn.close()

    def update_role(self, role: Role) -> None:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE roles SET role_name = %s WHERE role_id = %s", (role.role_name, role.role_id))
        conn.commit()
        cursor.close()
        conn.close()

    def get_role(self, role_id: str) -> Role:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT role_id, role_name FROM roles WHERE role_id = %s", (role_id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return Role(role_id=row[0], role_name=row[1])

    def get_all_roles(self) -> list[Role]:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT role_id, role_name FROM roles")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [Role(role_id=row[0], role_name=row[1]) for row in rows]