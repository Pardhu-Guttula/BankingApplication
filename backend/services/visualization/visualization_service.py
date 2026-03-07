# Epic Title: Banking Platform — Core API

import matplotlib.pyplot as plt
from backend.models.interaction_history.interaction_record import InteractionRecord
from typing import List
from datetime import datetime

class VisualizationService:
    @staticmethod
    def visualize_interaction_history(interactions: List[InteractionRecord], interaction_type: str) -> str:
        dates = [datetime.strptime(interaction.timestamp, '%Y-%m-%d %H:%M:%S') for interaction in interactions]
        plt.figure(figsize=(10, 5))
        
        if interaction_type == "login":
            plt.title("Login History Over Time")
        elif interaction_type == "page_visit":
            plt.title("Page Visit History Over Time")
        elif interaction_type == "form_submission":
            plt.title("Form Submission History Over Time")

        plt.hist(dates, bins=30, alpha=0.7, color='b', rwidth=0.85)
        plt.xlabel('Date')
        plt.ylabel(f'Number of {interaction_type.capitalize()}s')
        plt.grid(True)
        
        filename = f"{interaction_type}_history.png"
        plt.savefig(filename)
        plt.close()
        
        return filename