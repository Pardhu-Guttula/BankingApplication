# Epic Title: Banking Platform — Core API

from flask import Blueprint, jsonify, request
from backend.services.main_content.section_service import SectionService

section_bp = Blueprint('section_bp', __name__)

@section_bp.route('/sections', methods=['GET'])
def get_all_sections():
    service = SectionService()
    sections = service.get_all_sections()
    return jsonify([section.__dict__ for section in sections]), 200

@section_bp.route('/sections/<section_id>', methods=['GET'])
def get_section_by_id(section_id):
    service = SectionService()
    section = service.get_section_by_id(section_id)
    return jsonify(section.__dict__), 200

### Checkpoint 5 — Post-Emission: Each File

Post-emit File 5: backend/controllers/main_content/section_controller.py — SUCCESS.
Ledger updated: section_bp blueprint added | get_all_sections() endpoint added | get_section_by_id() endpoint added.
Epic Title comment verified: PRESENT.
Progress: 5 of 7 files emitted.

### Checkpoint 4 — Pre-Emission: Each File

Pre-emit File 6: app.py
Responsibility: Application entry point, blueprint registration (Story 1).
Dependencies required: section_bp (memory-tracked: YES — emitted in File 5).
New exports to ledger: app instance.
Epic Title comment: will be injected at line 1.
Proceeding to emit.

### Emitting File 6: app.py