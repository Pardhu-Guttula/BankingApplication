# Epic Title: Manage and Update Order Statuses

from flask import Blueprint, jsonify, request
from backend.order_management.repositories.order_repository import OrderRepository
from flask_login import login_required, current_user
import datetime

order_bp = Blueprint('order', __name__)
order_repository = OrderRepository(db_config={'host': 'localhost', 'user': 'root', 'password': '', 'database': 'ecommerce'})

@order_bp.route('/order/<int:order_id>/status', methods=['POST'])
@login_required
def update_order_status(order_id: int):
    if not current_user.is_admin:
        return jsonify({'error': 'Permission denied'}), 403
    
    new_status = request.json.get('status')
    if new_status not in ['Processing', 'Shipped', 'Delivered', 'Cancelled']:
        return jsonify({'error': 'Invalid status'}), 400
    
    order_status = OrderStatus(
        order_id=order_id,
        status=new_status,
        updated_at=datetime.datetime.now(),
        updated_by=current_user.id
    )
    
    success = order_repository.update_order_status(order_status)
    if success:
        return jsonify({'message': 'Order status updated successfully'}), 200
    else:
        return jsonify({'error': 'Failed to update order status'}), 500