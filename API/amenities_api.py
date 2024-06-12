from flask import Flask, request, jsonify
import json
import os
from class_amenities import amenities
app = Flask(__name__)
data_file = 'data/amenities.json'

def load_data():
    if os.path.exists(data_file):
        with open(data_file, 'r') as f:
            return json.load(f)
    return []

def save_data(data):
    with open(data_file, 'w') as f:
        json.dump(data, f)

@app.route('/amenities', methods=['GET'])
def get_amenities():
    amenities = load_data()
    return jsonify(amenities), 200

@app.route('/amenities/<int:amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    amenities = load_data()
    amenity = next((a for a in amenities if a['ID'] == amenity_id), None)
    if amenity:
        return jsonify(amenity), 200
    return jsonify({'error': 'Amenity not found'}), 404

@app.route('/amenities', methods=['POST'])
def create_amenity():
    new_amenity = request.json
    amenities = load_data()
    if any(a['ID'] == new_amenity['ID'] for a in amenities):
        return jsonify({'error': 'ID already exists'}), 400
    amenities.append(new_amenity)
    save_data(amenities)
    return jsonify(new_amenity), 201

@app.route('/amenities/<int:amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    updated_amenity = request.json
    amenities = load_data()
    for i, amenity in enumerate(amenities):
        if amenity['ID'] == amenity_id:
            amenities[i] = updated_amenity
            save_data(amenities)
            return jsonify(updated_amenity), 200
    return jsonify({'error': 'Amenity not found'}), 404

@app.route('/amenities/<int:amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    amenities = load_data()
    amenities = [a for a in amenities if a['ID'] != amenity_id]
    save_data(amenities)
    return jsonify({'message': 'Amenity deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)
