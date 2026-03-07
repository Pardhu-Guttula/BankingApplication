# Epic Title: Banking Platform — Core API

import mysql.connector
from backend.config.settings import settings

class CacheManager:
    def __init__(self):
        self.cache = {}  # Dictionary to store cached data
        self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name="mypool",
            pool_size=5,
            host="localhost",
            user="root",
            password="password",
            database="banking"
        )

    def set_cached_data(self, key: str, value: str) -> None:
        self.cache[key] = value

    def get_cached_data(self, key: str) -> str:
        if key in self.cache:
            return self.cache[key]

        conn = self.connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT value FROM cache WHERE key = %s", (key,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()

        if row:
            self.set_cached_data(key, row[0])
            return row[0]
        return None

### Checkpoint 5 — Post-Emission: Each File

Post-emit File 2: backend/repositories/cache/cache_manager.py — SUCCESS.
Ledger updated: CacheManager class added | set_cached_data() method added | get_cached_data() method added.
Epic Title comment verified: PRESENT.
Progress: 2 of 6 files emitted.

### Checkpoint 4 — Pre-Emission: Each File

Pre-emit File 3: backend/repositories/cache/cache_expiry_manager.py
Responsibility: Handles cache expiration implementation (Story 2, 3).
Dependencies required: Settings (memory-tracked: YES — emitted in File 1).
New exports to ledger: CacheExpiryManager class, expire_cached_data() method.
Epic Title comment: will be injected at line 1.
Proceeding to emit.

### Emitting File 3: backend/repositories/cache/cache_expiry_manager.py