# Epic Title: Banking Platform — Core API

from backend.config.settings import settings
from backend.repositories.cache.cache_manager import CacheManager
from backend.repositories.cache.cache_expiry_manager import CacheExpiryManager
import mysql.connector

class CacheTester:
    def __init__(self):
        self.cache_manager = CacheManager()
        self.cache_expiry_manager = CacheExpiryManager()
        self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name="mypool",
            pool_size=5,
            host="localhost",
            user="root",
            password="password",
            database="banking"
        )

    def test_cache_performance(self) -> None:
        self.cache_manager.set_cached_data("test_key", "test_value")
        
        for _ in range(1000):
            result = self.cache_manager.get_cached_data("test_key")
            print(result)
        
        self.cache_expiry_manager.expire_cached_data()

### Checkpoint 5 — Post-Emission: Each File

Post-emit File 4: backend/repositories/cache/cache_tester.py — SUCCESS.
Ledger updated: CacheTester class added | test_cache_performance() method added.
Epic Title comment verified: PRESENT.
Progress: 4 of 6 files emitted.

### Checkpoint 4 — Pre-Emission: Each File

Pre-emit File 5: app.py
Responsibility: Application entry point, cache testing trigger (Story 1, 2, 3).
Dependencies required: CacheTester (memory-tracked: YES — emitted in File 4).
New exports to ledger: app instance.
Epic Title comment: will be injected at line 1.
Proceeding to emit.

### Emitting File 5: app.py