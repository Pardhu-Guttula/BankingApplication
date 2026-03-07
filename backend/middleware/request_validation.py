# Epic Title: Banking Platform — Core API

from flask import request, jsonify

def validate_account_opening_request(func):
    def wrapper(*args, **kwargs):
        data = request.json
        if 'user_id' not in data or 'account_type' not in data or 'initial_deposit' not in data:
            return jsonify({"message": "Invalid data"}), 400
        return func(*args, **kwargs)
    return wrapper