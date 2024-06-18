from flask import Flask, request, jsonify, abort
from amenitie_data_manager import AmenitieDataManager
from Model.Class.amenitie import Amenitie # type: ignore

app = Flask(__name__)
amenitie_data_manager = AmenitieDataManager()

@app.route("/amenities", methods=["POST"])
def create_amenitie():
    data = request.get_json()
    if not data or "name" not in data:
        abort(400, "Missing required fields.")
    
    name = data["name"]
    if not name:
        abort(400, "Name cannot be empty.")
    
    amenitie_id = len(amenitie_data_manager.get_all()) + 1
    amenitie = Amenitie(amenitie_id=amenitie_id, name=name)
    amenitie_data_manager.save(amenitie)
    
    return jsonify({
        "id": amenitie.amenitie_id,
        "name": amenitie.name,
        "created_at": amenitie.created_at,
        "updated_at": amenitie.updated_at,
    }), 201

@app.route("/amenities", methods=["GET"])
def list_amenities():
    amenities = amenitie_data_manager.get_all()
    amenities_list = [{
        "id": amenitie.amenitie_id,
        "name": amenitie.name,
        "created_at": amenitie.created_at,
        "updated_at": amenitie.updated_at,
    } for amenitie in amenities]
    
    return jsonify(amenities_list), 200

@app.route("/amenities/<int:amenitie_id>", methods=["GET"])
def get_amenitie(amenitie_id):
    amenitie = amenitie_data_manager.get(amenitie_id)
    if not amenitie:
        abort(404, "Amenitie not found.")
    
    return jsonify({
        "id": amenitie.amenitie_id,
        "name": amenitie.name,
        "created_at": amenitie.created_at,
        "updated_at": amenitie.updated_at,
    }), 200

@app.route("/amenities/<int:amenitie_id>", methods=["PUT"])
def update_amenitie(amenitie_id):
    amenitie = amenitie_data_manager.get(amenitie_id)
    if not amenitie:
        abort(404, "Amenitie not found.")
    
    data = request.get_json()
    if not data or "name" not in data:
        abort(400, "Missing required fields.")
    
    name = data["name"]
    if not name:
        abort(400, "Name cannot be empty.")
    
    amenitie.name = name
    amenitie_data_manager.update(amenitie)
    
    return jsonify({
        "id": amenitie.amenitie_id,
        "name": amenitie.name,
        "created_at": amenitie.created_at,
        "updated_at": amenitie.updated_at,
    }), 200

@app.route("/amenities/<int:amenitie_id>", methods=["DELETE"])
def delete_amenitie(amenitie_id):
    amenitie = amenitie_data_manager.get(amenitie_id)
    if not amenitie:
        abort(404, "Amenitie not found.")
    
    amenitie_data_manager.delete(amenitie_id)
    return '', 204

if __name__ == "__main__":
    app.run(debug=True)