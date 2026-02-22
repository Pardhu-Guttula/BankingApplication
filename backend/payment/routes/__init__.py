# Epic Title: Integrate payment gateway (Stripe) for processing payments

from flask import Flask
from backend.payment.controllers.payment_controller import payment_bp

app = Flask(__name__)
app.register_blueprint(payment_bp)