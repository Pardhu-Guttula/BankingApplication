# Epic Title: Create User Table in PostgreSQL

from flask import Flask
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from backend.database.config import Base, engine, get_db
from backend.authentication.repositories.user_repository import UserRepository
from backend.authentication.services.registration_service import RegistrationService

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register_user():
    db: Session = next(get_db())
    user_repository = UserRepository(db)
    registration_service = RegistrationService(user_repository)

    try:
        data = request.get_json()

        name = data['name']
        email = data['email']
        password = data['password']

        new_user = registration_service.register_user(db, name, email, password)
        return jsonify({"message": "User registered successfully"}), 201
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except SQLAlchemyError as se:
        return jsonify({"error": "Database error occurred"}), 500
    except KeyError:
        return jsonify({"error": "Invalid input data"}), 400

@app.before_first_request
def startup():
    # Create all tables in the database
    Base.metadata.create_all(bind=engine)

@app.teardown_appcontext
def shutdown(exception):
    # Code to run on shutdown, e.g., close db connection, clean up resources
    pass

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)