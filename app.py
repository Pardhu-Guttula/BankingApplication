# Epic Title: Implement user authentication and authorization features

from backend.authentication.controllers.login_controller import app as login_app
from backend.authentication.controllers.logout_controller import app as logout_app
from backend.access_control.controllers.role_controller import app as role_app

if __name__ == "__main__":
    login_app.run(debug=True)
    logout_app.run(debug=True)
    role_app.run(debug=True)