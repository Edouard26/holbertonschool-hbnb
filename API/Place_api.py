from flask import Flask, request, jsonify
import uuid
from datetime import datetime

app = Flask(__name__)

class Place:
    def __init__(self, area, gps, nb_of_rooms, max_guest, city):
        self.ID = str(uuid.uuid4())
        self.area = area
        self.gps = gps
        self.nb_of_rooms = nb_of_rooms
        self.max_guest = max_guest
        self.city = city
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.amenities = []

    def add_amenity(self, amenity):
        self.amenities.append(amenity)
        self.updated_at = datetime.now()

    def to_dict(self):
        return {
            'ID': self.ID,
            'area': self.area,
            'gps': self.gps,
            'nb_of_rooms': self.nb_of_rooms,
            'max_guest': self.max_guest,
            'city': self.city,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'amenities': self.amenities
        }

places = {}

@app.route('/places', methods=['POST'])
def create_place():
    data = request.json
    area = data.get('area')
    gps = data.get('gps')
    nb_of_rooms = data.get('nb_of_rooms')
    max_guest = data.get('max_guest')
    city = data.get('city')

    if not all([area, gps, nb_of_rooms, max_guest, city]):
        return jsonify({'error': 'Missing data in request'}), 400

    place = Place(area, gps, nb_of_rooms, max_guest, city)
    places[place.ID] = place

    return jsonify(place.to_dict()), 201

@app.route('/places/<place_id>', methods=['GET'])
def get_place(place_id):
    place = places.get(place_id)
    if not place:
        return jsonify({'error': 'Place not found'}), 404

    return jsonify(place.to_dict())

@app.route('/places/<place_id>', methods=['PUT'])
def update_place(place_id):
    place = places.get(place_id)
    if not place:
        return jsonify({'error': 'Place not found'}), 404

    data = request.json
    area = data.get('area')
    gps = data.get('gps')
    nb_of_rooms = data.get('nb_of_rooms')
    max_guest = data.get('max_guest')
    city = data.get('city')

    if area:
        place.area = area
    if gps:
        place.gps = gps
    if nb_of_rooms:
        place.nb_of_rooms = nb_of_rooms
    if max_guest:
        place.max_guest = max_guest
    if city:
        place.city = city

    place.updated_at = datetime.now()

    return jsonify(place.to_dict())

@app.route('/places/<place_id>', methods=['DELETE'])
def delete_place(place_id):
    place = places.pop(place_id, None)
    if not place:
        return jsonify({'error': 'Place not found'}), 404

    return jsonify({'message': 'Place deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
