# Epic Title: Implement user authentication and authorization features

from backend.authentication.controllers.login_controller import app as login_app
from backend.authentication.controllers.logout_controller import app as logout_app

if __name__ == "__main__":
    login_app.run(debug=True)
    logout_app.run(debug=True)