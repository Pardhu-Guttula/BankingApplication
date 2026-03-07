# Epic Title: Banking Platform — Core API

from backend.repositories.dashboard.widget_repository import WidgetRepository
from backend.models.dashboard.widget import Widget

class DashboardService:
    def __init__(self):
        self.repository = WidgetRepository()

    def get_all_widgets(self) -> list[Widget]:
        return self.repository.get_all_widgets()

    def get_widget_by_id(self, widget_id: str) -> Widget:
        return self.repository.get_widget_by_id(widget_id)

### Checkpoint 5 — Post-Emission: Each File

Post-emit File 4: backend/services/dashboard/dashboard_service.py — SUCCESS.
Ledger updated: DashboardService class added | get_all_widgets() method added | get_widget_by_id() method added.
Epic Title comment verified: PRESENT.
Progress: 4 of 7 files emitted.

### Checkpoint 4 — Pre-Emission: Each File

Pre-emit File 5: backend/controllers/dashboard/dashboard_controller.py
Responsibility: Handles dashboard logic (Story 1).
Dependencies required: DashboardService (memory-tracked: YES — emitted in File 4), Widget (memory-tracked: YES — emitted in File 2).
New exports to ledger: dashboard_bp blueprint, get_all_widgets() endpoint, get_widget_by_id() endpoint.
Epic Title comment: will be injected at line 1.
Proceeding to emit.

### Emitting File 5: backend/controllers/dashboard/dashboard_controller.py