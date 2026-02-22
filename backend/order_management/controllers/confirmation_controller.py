# Epic Title: Display order confirmation to customers after successful payment

from flask import Blueprint, jsonify, request, render_template
from backend.order_management.repositories.order_repository import OrderRepository
import smtplib
from email.mime.text import MIMEText

confirmation_bp = Blueprint('confirmation', __name__)
order_repository = OrderRepository(db_config={'host': 'localhost', 'user': 'root', 'password': '', 'database': 'ecommerce'})

@confirmation_bp.route('/confirmation/<int:order_id>', methods=['GET'])
def display_confirmation(order_id: int):
    order = order_repository.get_order_by_id(order_id)
    
    if order is None:
        return jsonify({'error': 'Order not found'}), 404
    
    return render_template('confirmation.html', order=order)


def send_confirmation_email(order):
    msg = MIMEText(f"Order Confirmation\n\nOrder ID: {order.order_id}\nTransaction ID: {order.transaction_id}\nItems:\n" + "\n".join([f"{item.name} x {item.quantity} - ${item.price}" for item in order.items]) + f"\nTotal Amount: ${order.total_amount}")
    msg['Subject'] = 'Order Confirmation'
    msg['From'] = 'no-reply@ecommerce.com'
    msg['To'] = order.customer_email

    with smtplib.SMTP('localhost') as server:
        server.sendmail('no-reply@ecommerce.com', [order.customer_email], msg.as_string())

@confirmation_bp.route('/confirmation/email/<int:order_id>', methods=['POST'])
def send_confirmation(order_id: int):
    order = order_repository.get_order_by_id(order_id)

    if order is None:
        return jsonify({'error': 'Order not found'}), 404

    send_confirmation_email(order)
    return jsonify({'success': 'Email sent successfully'}), 200