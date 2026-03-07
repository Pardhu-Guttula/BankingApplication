# Epic Title: Banking Platform — Core API

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from cryptography.fernet import Fernet
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
        self.encryption_key = settings.ENCRYPTION_KEY
        self.cipher = Fernet(self.encryption_key.encode())

    def encrypt_content(self, content: str) -> str:
        return self.cipher.encrypt(content.encode()).decode()

    def decrypt_content(self, encrypted_content: str) -> str:
        return self.cipher.decrypt(encrypted_content.encode()).decode()

    def send_email(self, email_id: str, subject: str, body: str, to_email: str) -> DeliveryReceipt:
        encrypted_body = self.encrypt_content(body)
        
        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(encrypted_body, 'plain'))
        
        retries = 3
        for attempt in range(retries):
            try:
                with smtplib.SMTP(self.server, self.port) as server:
                    server.starttls()
                    server.login(self.username, self.password)
                    server.sendmail(self.username, to_email, msg.as_string())
                    receipt = DeliveryReceipt(receipt_id=email_id, email=to_email, status='Delivered')
                    self.repository.save_delivery_receipt(receipt)
                    self.repository.update_email_status(email_id=email_id, status='Delivered')
                    return receipt
            except Exception as e:
                if attempt == retries - 1:
                    receipt = DeliveryReceipt(receipt_id=email_id, email=to_email, status='Failed')
                    self.repository.save_delivery_receipt(receipt)
                    self.repository.update_email_status(email_id=email_id, status='Failed')
                    return receipt