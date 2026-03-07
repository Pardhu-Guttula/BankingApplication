# Epic Title: Banking Platform — Core API

from backend.repositories.interaction_history.interaction_repository import InteractionRepository
from backend.models.interaction_history.interaction_record import InteractionRecord
import csv
import pdfkit

class InteractionService:
    def __init__(self):
        self.repository = InteractionRepository()

    def get_interactions(self, user_id: str, date_start: str = None, date_end: str = None) -> list[InteractionRecord]:
        return self.repository.get_interactions(user_id, date_start, date_end)

    def export_interactions_csv(self, user_id: str, date_start: str = None, date_end: str = None) -> str:
        interactions = self.get_interactions(user_id, date_start, date_end)
        file_path = f'/tmp/{user_id}_interactions.csv'
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['interaction_id', 'user_id', 'interaction_type', 'timestamp'])
            for interaction in interactions:
                writer.writerow([interaction.interaction_id, interaction.user_id, interaction.interaction_type, interaction.timestamp])
        return file_path

    def export_interactions_pdf(self, user_id: str, date_start: str = None, date_end: str = None) -> str:
        interactions = self.get_interactions(user_id, date_start, date_end)
        html_content = "<html><body><h1>Interaction History</h1><table><tr><th>Interaction ID</th><th>User ID</th><th>Interaction Type</th><th>Timestamp</th></tr>"
        for interaction in interactions:
            html_content += f"<tr><td>{interaction.interaction_id}</td><td>{interaction.user_id}</td><td>{interaction.interaction_type}</td><td>{interaction.timestamp}</td></tr>"
        html_content += "</table></body></html>"
        file_path = f'/tmp/{user_id}_interactions.pdf'
        pdfkit.from_string(html_content, file_path)
        return file_path