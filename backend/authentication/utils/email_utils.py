# Epic Title: Develop User Registration Capability

import smtplib
from email.mime.text import MIMEText

def send_confirmation_email(email: str):
    msg = MIMEText("Thank you for registering. Please confirm your email address.")
    msg['Subject'] = 'Email Confirmation'
    msg['From'] = 'noreply@example.com'
    msg['To'] = email

    with smtplib.SMTP('localhost') as server:
        server.sendmail('noreply@example.com', email, msg.as_string())