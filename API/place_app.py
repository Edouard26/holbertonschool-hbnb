from flask import Flask, request, jsonify, abort
from places_data_manager import PlaceDataManager
from Model.Class.place import Place

app = Flask(__name__)
place_data_manager = PlaceDataManager()

@app.route("/place", methods=["POST"])
def create_place():
    data = request.get_json()
    if not data or "name" not in data:
        abort(400, "Missing required fields.")
    
    name = data["name"]
    if not name:
        abort(400, "Name cannot be empty.")
    
    place_id = len(places_data_manager.get_all()) + 1
    place = Place(place_id=place_id, name=name)
    place_data_manager.save(place)
    
    return jsonify({
        "id": place.place_id,
        "name": place.name,
        "created_at": place.created_at,
        "updated_at": place.updated_at,
    }), 201

@app.route("/place", methods=["GET"])
def list_places():
    place = place_data_manager.get_all()
    place_list = [{
        "id": place.place_id,
        "name": place.name,
        "created_at": place.created_at,
        "updated_at": place.updated_at,
    } for place in place]
    
    return jsonify(places_list), 200

@app.route("/place/<int:place_id>", methods=["GET"])
def get_place(place_id):
    place = place_data_manager.get(place_id)
    if not place:
        abort(404, "Place not found.")
    
    return jsonify({
        "id": place.place_id,
        "name": place.name,
        "created_at": place.created_at,
        "updated_at": place.updated_at,
    }), 200

@app.route("/place/<int:place_id>", methods=["PUT"])
def update_place(place_id):
    places = place_data_manager.get(place_id)
    if not place:
        abort(404, "Place not found.")
    
    data = request.get_json()
    if not data or "name" not in data:
        abort(400, "Missing required fields.")
    
    name = data["name"]
    if not name:
        abort(400, "Name cannot be empty.")
    
    place.name = name
    place_data_manager.update(place)
    
    return jsonify({
        "id": place.place_id,
        "name": place.name,
        "created_at": place.created_at,
        "updated_at": place.updated_at,
    }), 200

@app.route("/place/<int:place_id>", methods=["DELETE"])
def delete_place(place_id):
    place = place_data_manager.get(place_id)
    if not place:
        abort(404, "Place not found.")
    
    place_data_manager.delete(place_id)
    return '', 204

if __name__ == "__main__":
    app.run(debug=True)