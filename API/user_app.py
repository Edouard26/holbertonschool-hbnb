from flask import Flask, request, jsonify, abort
from user_data_manager import UserDataManager
from Model.Class.user import User

app = Flask(__name__)
user_data_manager = UserDataManager()

def is_valid_email(email):
    import re
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    if not data or not all(k in data for k in ("email", "first_name", "last_name")):
        abort(400, "Missing required fields.")
    
    email = data["email"]
    first_name = data["first_name"]
    last_name = data["last_name"]
    
    if not email or not is_valid_email(email):
        abort(400, "Invalid email.")
    if not first_name or not last_name:
        abort(400, "First name and last name cannot be empty.")
    

    for user in user_data_manager.get_all():
        if user.email == email:
            abort(409, "Email already exists.")
    
    user_id = len(user_data_manager.get_all()) + 1
    user = User(user_id=user_id, email=email, first_name=first_name, last_name=last_name)
    user_data_manager.save(user)
    
    return jsonify({
        "id": user.user_id,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "created_at": user.created_at,
        "updated_at": user.updated_at,
    }), 201

@app.route("/users", methods=["GET"])
def list_users():
    users = user_data_manager.get_all()
    users_list = [{
        "id": user.user_id,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "created_at": user.created_at,
        "updated_at": user.updated_at,
    } for user in users]
    
    return jsonify(users_list), 200

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = user_data_manager.get(user_id)
    if not user:
        abort(404, "User not found.")
    
    return jsonify({
        "id": user.user_id,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "created_at": user.created_at,
        "updated_at": user.updated_at,
    }), 200

@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = user_data_manager.get(user_id)
    if not user:
        abort(404, "User not found.")
    
    data = request.get_json()
    if not data:
        abort(400, "Missing required fields.")
    
    email = data.get("email", user.email)
    first_name = data.get("first_name", user.first_name)
    last_name = data.get("last_name", user.last_name)
    
    if not email or not is_valid_email(email):
        abort(400, "Invalid email.")
    if not first_name or not last_name:
        abort(400, "First name and last name cannot be empty.")
    

    for existing_user in user_data_manager.get_all():
        if existing_user.email == email and existing_user.user_id != user_id:
            abort(409, "Email already exists.")
    
    user.email = email
    user.first_name = first_name
    user.last_name = last_name
    user_data_manager.update(user)
    
    return jsonify({
        "id": user.user_id,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "created_at": user.created_at,
        "updated_at": user.updated_at,
    }), 200

@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = user_data_manager.get(user_id)
    if not user:
        abort(404, "User not found.")
    
    user_data_manager.delete(user_id)
    return '', 204

if __name__ == "__main__":
    app.run(debug=True)