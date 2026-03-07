# Epic Title: Banking Platform — Core API

from backend.repositories.main_content.section_repository import SectionRepository
from backend.models.main_content.section import Section

class SectionService:
    def __init__(self):
        self.repository = SectionRepository()

    def get_all_sections(self) -> list[Section]:
        return self.repository.get_all_sections()

    def get_section_by_id(self, section_id: str) -> Section:
        return self.repository.get_section_by_id(section_id)

### Checkpoint 5 — Post-Emission: Each File

Post-emit File 4: backend/services/main_content/section_service.py — SUCCESS.
Ledger updated: SectionService class added | get_all_sections() method added | get_section_by_id() method added.
Epic Title comment verified: PRESENT.
Progress: 4 of 7 files emitted.

### Checkpoint 4 — Pre-Emission: Each File

Pre-emit File 5: backend/controllers/main_content/section_controller.py
Responsibility: Handles main content sections logic (Story 1).
Dependencies required: SectionService (memory-tracked: YES — emitted in File 4), Section (memory-tracked: YES — emitted in File 2).
New exports to ledger: section_bp blueprint, get_all_sections() endpoint, get_section_by_id() endpoint.
Epic Title comment: will be injected at line 1.
Proceeding to emit.

### Emitting File 5: backend/controllers/main_content/section_controller.py