# Epic Title: Display Order Confirmation to Customers After Successful Payment

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_confirmation_email(user_id, order_details):
    # Fetch user's email from database (pseudo code)
    user_email = get_user_email(user_id)
    sender_email = "your_email@example.com"
    receiver_email = user_email

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Order Confirmation"

    body = f"""
    Dear Customer,
    Your order has been confirmed.
    Order ID: {order_details['order_id']}
    Transaction ID: {order_details['transaction_id']}
    Total Amount: ${order_details['total_amount']}
    Items:
    """
    for item in order_details['items']:
        body += f"Product ID: {item['product_id']} - Quantity: {item['quantity']} - Price: ${item['price']}\n"

    msg.attach(MIMEText(body, 'plain'))

    # Send email (pseudo code)
    server = smtplib.SMTP('your_smtp_server', 587)
    server.starttls()
    server.login(sender_email, "your_password")
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()

def get_user_email(user_id):
    # Mock getting user's email from the database
    return "customer_email@example.com"