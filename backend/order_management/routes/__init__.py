# Epic Title: Display order confirmation to customers after successful payment

from flask import Flask
from backend.order_management.controllers.confirmation_controller import confirmation_bp

app = Flask(__name__)
app.register_blueprint(confirmation_bp)
app.config['TEMPLATES_AUTO_RELOAD'] = True