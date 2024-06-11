from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
data_file = 'data/cities.json'

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

# Get all cities
@app.route('/cities', methods=['GET'])
def get_cities():
    cities = load_data()
    return jsonify(cities), 200

# Get city by ID
@app.route('/cities/<int:city_id>', methods=['GET'])
def get_city(city_id):
    cities = load_data()
    city = next((c for c in cities if c['ID'] == city_id), None)
    if city:
        return jsonify(city), 200
    return jsonify({'error': 'City not found'}), 404

# Create a new city
@app.route('/cities', methods=['POST'])
def create_city():
    new_city = request.json
    cities = load_data()
    if any(c['ID'] == new_city['ID'] for c in cities):
        return jsonify({'error': 'ID already exists'}), 400
    cities.append(new_city)
    save_data(cities)
    return jsonify(new_city), 201

# Update a city
@app.route('/cities/<int:city_id>', methods=['PUT'])
def update_city(city_id):
    updated_city = request.json
    cities = load_data()
    for i, city in enumerate(cities):
        if city['ID'] == city_id:
            cities[i] = updated_city
            save_data(cities)
            return jsonify(updated_city), 200
    return jsonify({'error': 'City not found'}), 404

# Delete a city
@app.route('/cities/<int:city_id>', methods=['DELETE'])
def delete_city(city_id):
    cities = load_data()
    cities = [c for c in cities if c['ID'] != city_id]
    save_data(cities)
    return jsonify({'message': 'City deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)
