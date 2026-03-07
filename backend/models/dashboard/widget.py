# Epic Title: Banking Platform — Core API

class Widget:
    def __init__(self, widget_id: str, name: str, data: str):
        self.widget_id = widget_id
        self.name = name
        self.data = data

### Checkpoint 5 — Post-Emission: Each File

Post-emit File 2: backend/models/dashboard/widget.py — SUCCESS.
Ledger updated: Widget class added.
Epic Title comment verified: PRESENT.
Progress: 2 of 7 files emitted.

### Checkpoint 4 — Pre-Emission: Each File

Pre-emit File 3: backend/repositories/dashboard/widget_repository.py
Responsibility: DB queries for dashboard widgets (Story 1).
Dependencies required: Widget (memory-tracked: YES — emitted in File 2).
New exports to ledger: WidgetRepository class, get_all_widgets(), get_widget_by_id() methods.
Epic Title comment: will be injected at line 1.
Proceeding to emit.

### Emitting File 3: backend/repositories/dashboard/widget_repository.py