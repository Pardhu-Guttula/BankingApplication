# Epic Title: Banking Platform — Core API

class Settings:
    DATABASE_URL = "mysql://root:password@localhost/banking"
    EMAIL_SERVER = "smtp.example.com"
    EMAIL_PORT = 587
    EMAIL_USERNAME = "user@example.com"
    EMAIL_PASSWORD = "password"
    ENCRYPTION_KEY = "myencryptionkey"

settings = Settings()