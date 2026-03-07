# Epic Title: Banking Platform — Core API

from backend.repositories.interaction_history.interaction_repository import InteractionRepository
from backend.models.interaction_history.interaction_record import InteractionRecord
import smtplib
from email.mime.text import MIMEText

class AnomalyDetectionService:
    def __init__(self):
        self.repository = InteractionRepository()

    def notify_admin(self, subject: str, body: str):
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = "noreply@example.com"
        msg["To"] = Settings.ADMIN_EMAIL

        with smtplib.SMTP("localhost") as server:
            server.sendmail("noreply@example.com", [Settings.ADMIN_EMAIL], msg.as_string())

    def detect_anomalies(self):
        failed_logins = self.repository.get_failed_logins()
        if len(failed_logins) > 5:  # Arbitrary threshold for multiple failed logins
            self.notify_admin("Anomaly Detected: Multiple Failed Logins", "Multiple failed logins detected in the system. Please investigate.")

        unusual_locations = self.repository.get_unusual_locations()
        if unusual_locations:
            self.notify_admin("Anomaly Detected: Unusual Location Access", "Unusual geographic location access detected. Please investigate.")

        repeated_exports = self.repository.get_repeated_exports()
        if repeated_exports:
            self.notify_admin("Anomaly Detected: Repeated Data Export Attempts", "Repeated data export attempts detected within a short period. Please investigate.")