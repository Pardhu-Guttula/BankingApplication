# Epic Title: Banking Platform — Core API

from backend.repositories.interaction_history.interaction_repository import InteractionRepository
from backend.models.interaction_history.interaction_record import InteractionRecord
import smtplib
from email.mime.text import MIMEText

class DataRetentionService:
    def __init__(self):
        self.repository = InteractionRepository()

    def notify_admin(self, subject: str, body: str):
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = "noreply@example.com"
        msg["To"] = Settings.ADMIN_EMAIL

        with smtplib.SMTP("localhost") as server:
            server.sendmail("noreply@example.com", [Settings.ADMIN_EMAIL], msg.as_string())

    def delete_old_records(self):
        old_records = self.repository.get_records_for_deletion()
        for record in old_records:
            self.repository.delete_record(record.interaction_id)
            self.notify_admin(
                "Data Deletion Notification",
                f"Interaction record {record.interaction_id} has been deleted due to retention policy."
            )

    def generate_compliance_report(self) -> str:
        records = self.repository.get_records_for_compliance()
        report = "Interaction Records Compliance Report:\n\n"
        for record in records:
            report += f"{record.interaction_id}, {record.user_id}, {record.interaction_type}, {record.timestamp}, {record.location}\n"
        return report

    def notify_before_deletion(self):
        old_records = self.repository.get_records_for_deletion()
        for record in old_records:
            self.notify_admin(
                "Upcoming Data Deletion Notification",
                f"Interaction record {record.interaction_id} will be deleted soon due to retention policy."
            )