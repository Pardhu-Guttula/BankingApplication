# Epic Title: Banking Platform — Core API

import mysql.connector
from backend.config.settings import settings

class CacheExpiryManager:
    def __init__(self):
        self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name="mypool",
            pool_size=5,
            host="localhost",
            user="root",
            password="password",
            database="banking"
        )

    def expire_cached_data(self) -> None:
        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM cache WHERE updated_at < NOW() - INTERVAL %s SECOND", (settings.CACHE_EXPIRY_TIME,))
        conn.commit()
        cursor.close()
        conn.close()

### Checkpoint 5 — Post-Emission: Each File

Post-emit File 3: backend/repositories/cache/cache_expiry_manager.py — SUCCESS.
Ledger updated: CacheExpiryManager class added | expire_cached_data() method added.
Epic Title comment verified: PRESENT.
Progress: 3 of 6 files emitted.

### Checkpoint 4 — Pre-Emission: Each File

Pre-emit File 4: backend/repositories/cache/cache_tester.py
Responsibility: Handles cache performance testing under load (Story 3).
Dependencies required: CacheManager (memory-tracked: YES — emitted in File 2), CacheExpiryManager (memory-tracked: YES — emitted in File 3), Settings (memory-tracked: YES — emitted in File 1).
New exports to ledger: CacheTester class, test_cache_performance() method.
Epic Title comment: will be injected at line 1.
Proceeding to emit.

### Emitting File 4: backend/repositories/cache/cache_tester.py