# Epic Title: Implement user authentication and authorization features

from backend.authentication.controllers.login_controller import app

if __name__ == "__main__":
    app.run(debug=True)