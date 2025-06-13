#!/usr/bin/env python3
"""
task_05_basic_security.py

A simple Flask API demonstrating:
- Basic HTTP authentication using Flask-HTTPAuth
- Token-based authentication using Flask-JWT-Extended
- Role-based access control with in-memory user storage
- Secure password handling with Werkzeug
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required,
    get_jwt_identity, get_jwt
)
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta

app = Flask(__name__)
auth = HTTPBasicAuth()

app.config["JWT_SECRET_KEY"] = "super-secret-key"  # Replace with a strong key in production
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

jwt = JWTManager(app)

# In-memory user database
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """
    Verifies username and password for basic HTTP authentication.
    """
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return user
    return None


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """
    A route protected by basic HTTP authentication.
    """
    return jsonify(message="Basic Auth: Access Granted")


@app.route("/login", methods=["POST"])
def login():
    """
    Authenticates user credentials and returns a JWT token.
    Expects JSON with 'username' and 'password'.
    """
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    user = users.get(username)

    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_access_token(identity={"username": username, "role": user["role"]})
    return jsonify(access_token=token)


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """
    A route protected by JWT authentication.
    """
    return jsonify(message="JWT Auth: Access Granted")


@app.route("/admin-only")
@jwt_required()
def admin_only():
    """
    A route accessible only to users with the 'admin' role.
    """
    identity = get_jwt_identity()
    if identity["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return jsonify(message="Admin Access: Granted")


# === JWT ERROR HANDLERS ===

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """
    Handles missing JWTs.
    """
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """
    Handles invalid tokens.
    """
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    """
    Handles expired tokens.
    """
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    """
    Handles revoked tokens.
    """
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    """
    Handles requests that require a fresh token.
    """
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
