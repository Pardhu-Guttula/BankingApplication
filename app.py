# Epic Title: Banking Platform — Core API

from flask import Flask
from backend.repositories.database.performance_tester import PerformanceTester

app = Flask(__name__)

@app.route('/api/test', methods=['GET'])
def test_performance():
    tester = PerformanceTester()
    tester.test_performance()
    return "Performance test executed", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

### Checkpoint 5 — Post-Emission: Each File

Post-emit File 5: app.py — SUCCESS.
Ledger updated: app instance added.
Epic Title comment verified: PRESENT.
Progress: 5 of 6 files emitted.

### Checkpoint 4 — Pre-Emission: Each File

Pre-emit File 6: requirements.txt
Responsibility: Dependency listing (Story 1, 2, 3).
Dependencies required: flask, mysql-connector-python.
New exports to ledger: None (dependency-only file).
Epic Title comment: will be injected at line 1.
Proceeding to emit.

### Emitting File 6: requirements.txt