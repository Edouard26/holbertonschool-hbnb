from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
data_file = 'data/users.json'

# Load data from JSON file
def load_data():
    if os.path.exists(data_file):
        with open(data_file, 'r') as f:
            return json.load(f)
    return []

# Save data to JSON file
def save_data(data):
    with open(data_file, 'w') as f:
        json.dump(data, f)

# Get all users
@app.route('/users', methods=['GET'])
def get_users():
    users = load_data()
    return jsonify(users), 200

# Get user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    users = load_data()
    user = next((user for user in users if user['ID'] == user_id), None)
    if user:
        return jsonify(user), 200
    return jsonify({'error': 'User not found'}), 404

# Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    new_user = request.json
    users = load_data()
    if any(user['email'] == new_user['email'] for user in users):
        return jsonify({'error': 'Email already exists'}), 400
    users.append(new_user)
    save_data(users)
    return jsonify(new_user), 201

# Update a user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    updated_user = request.json
    users = load_data()
    for i, user in enumerate(users):
        if user['ID'] == user_id:
            users[i] = updated_user
            save_data(users)
            return jsonify(updated_user), 200
    return jsonify({'error': 'User not found'}), 404

# Delete a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    users = load_data()
    users = [user for user in users if user['ID'] != user_id]
    save_data(users)
    return jsonify({'message': 'User deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)
