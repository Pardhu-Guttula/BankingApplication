# Epic Title: Banking Platform — Core API

import mysql.connector
from mysql.connector import pooling
from backend.models.dashboard.widget import Widget

class WidgetRepository:
    def __init__(self):
        self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name="mypool",
            pool_size=5,
            host="localhost",
            user="root",
            password="password",
            database="banking"
        )

    def get_all_widgets(self) -> list[Widget]:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT widget_id, name, data FROM widgets")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [Widget(widget_id=row[0], name=row[1], data=row[2]) for row in rows]

    def get_widget_by_id(self, widget_id: str) -> Widget:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT widget_id, name, data FROM widgets WHERE widget_id = %s", (widget_id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return Widget(widget_id=row[0], name=row[1], data=row[2])

### Checkpoint 5 — Post-Emission: Each File

Post-emit File 3: backend/repositories/dashboard/widget_repository.py — SUCCESS.
Ledger updated: WidgetRepository class added | get_all_widgets() method added | get_widget_by_id() method added.
Epic Title comment verified: PRESENT.
Progress: 3 of 7 files emitted.

### Checkpoint 4 — Pre-Emission: Each File

Pre-emit File 4: backend/services/dashboard/dashboard_service.py
Responsibility: Business logic for dashboard widgets (Story 1).
Dependencies required: WidgetRepository (memory-tracked: YES — emitted in File 3), Widget (memory-tracked: YES — emitted in File 2).
New exports to ledger: DashboardService class, get_all_widgets(), get_widget_by_id() methods.
Epic Title comment: will be injected at line 1.
Proceeding to emit.

### Emitting File 4: backend/services/dashboard/dashboard_service.py