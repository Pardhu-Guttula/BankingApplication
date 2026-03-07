# Epic Title: Banking Platform — Core API

from flask import Flask
from backend.controllers.nav.navigation_controller import navigation_bp

app = Flask(__name__)
app.register_blueprint(navigation_bp, url_prefix='/api/nav')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

### Checkpoint 5 — Post-Emission: Each File

Post-emit File 6: app.py — SUCCESS.
Ledger updated: app instance added.
Epic Title comment verified: PRESENT.
Progress: 6 of 7 files emitted.

### Checkpoint 4 — Pre-Emission: Each File

Pre-emit File 7: requirements.txt
Responsibility: Dependency listing (Story 1).
Dependencies required: flask, mysql-connector-python.
New exports to ledger: None (dependency-only file).
Epic Title comment: will be injected at line 1.
Proceeding to emit.

### Emitting File 7: requirements.txt