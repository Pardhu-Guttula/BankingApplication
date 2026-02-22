# Epic Title: View Order History

from flask import Blueprint, jsonify, request
from backend.order_management.repositories.order_repository import OrderRepository
from flask_login import login_required, current_user

order_bp = Blueprint('order', __name__)
order_repository = OrderRepository(db_config={'host': 'localhost', 'user': 'root', 'password': '', 'database': 'ecommerce'})

@order_bp.route('/order/history', methods=['GET'])
@login_required
def view_order_history():
    user_id = current_user.id
    orders = order_repository.get_orders_by_user_id(user_id)
    
    if not orders:
        return jsonify({'message': 'You have no orders'}), 200
    
    order_history = []
    for order in orders:
        order_history.append({
            'order_id': order.order_id,
            'items': [{'item_id': item.id, 'name': item.name, 'price': item.price, 'quantity': item.quantity} for item in order.items],
            'total_amount': order.total_amount,
            'status': order.status
        })
    
    return jsonify({'orders': order_history}), 200