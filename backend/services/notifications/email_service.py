# Epic Title: Banking Platform — Core API

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from backend.repositories.notifications.notification_repository import NotificationRepository
from backend.models.notifications.delivery_receipt import DeliveryReceipt
from backend.config import settings

class EmailService:
    def __init__(self):
        self.repository = NotificationRepository()
        self.server = settings.EMAIL_SERVER
        self.port = settings.EMAIL_PORT
        self.username = settings.EMAIL_USERNAME
        self.password = settings.EMAIL_PASSWORD

    def send_email(self, template_id: str, to_email: str, context: dict) -> DeliveryReceipt:
        template = self.repository.get_email_template(template_id)
        if not template:
            raise ValueError("Invalid template id")
        
        subject = template.subject.format(**context)
        body = template.body.format(**context)
        
        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        retries = 3
        for attempt in range(retries):
            try:
                with smtplib.SMTP(self.server, self.port) as server:
                    server.starttls()
                    server.login(self.username, self.password)
                    server.sendmail(self.username, to_email, msg.as_string())
                    receipt = DeliveryReceipt(receipt_id='r-'+template_id, email=to_email, status='Delivered')
                    self.repository.save_delivery_receipt(receipt)
                    return receipt
            except Exception as e:
                if attempt == retries - 1:
                    receipt = DeliveryReceipt(receipt_id='r-'+template_id, email=to_email, status='Failed')
                    self.repository.save_delivery_receipt(receipt)
                    return receipt