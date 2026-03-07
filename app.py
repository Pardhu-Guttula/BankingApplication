# Epic Title: Banking Platform — Core API

from flask import Flask
from backend.controllers.interaction_history.interaction_controller import interaction_bp
from backend.controllers.notifications.notification_controller import notification_bp

app = Flask(__name__)
app.register_blueprint(interaction_bp, url_prefix='/api/interactions')
app.register_blueprint(notification_bp, url_prefix='/api/notifications')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)