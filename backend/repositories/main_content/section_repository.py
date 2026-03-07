# Epic Title: Banking Platform — Core API

import mysql.connector
from mysql.connector import pooling
from backend.models.main_content.section import Section

class SectionRepository:
    def __init__(self):
        self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name="mypool",
            pool_size=5,
            host="localhost",
            user="root",
            password="password",
            database="banking"
        )

    def get_all_sections(self) -> list[Section]:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT section_id, name, content FROM sections")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [Section(section_id=row[0], name=row[1], content=row[2]) for row in rows]

    def get_section_by_id(self, section_id: str) -> Section:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT section_id, name, content FROM sections WHERE section_id = %s", (section_id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return Section(section_id=row[0], name=row[1], content=row[2])

### Checkpoint 5 — Post-Emission: Each File

Post-emit File 3: backend/repositories/main_content/section_repository.py — SUCCESS.
Ledger updated: SectionRepository class added | get_all_sections() method added | get_section_by_id() method added.
Epic Title comment verified: PRESENT.
Progress: 3 of 7 files emitted.

### Checkpoint 4 — Pre-Emission: Each File

Pre-emit File 4: backend/services/main_content/section_service.py
Responsibility: Business logic for main content sections (Story 1).
Dependencies required: SectionRepository (memory-tracked: YES — emitted in File 3), Section (memory-tracked: YES — emitted in File 2).
New exports to ledger: SectionService class, get_all_sections(), get_section_by_id() methods.
Epic Title comment: will be injected at line 1.
Proceeding to emit.

### Emitting File 4: backend/services/main_content/section_service.py