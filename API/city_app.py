from flask import Flask, request, jsonify, abort
from city_data_manager import CityDataManager
from Model.Class.city import City

app = Flask(__name__)
city_data_manager = CityDataManager()

@app.route("/cities", methods=["POST"])
def create_city():
    data = request.get_json()
    if not data or "name" not in data:
        abort(400, "Missing required fields.")
    
    name = data["name"]
    if not name:
        abort(400, "Name cannot be empty.")
    
    city_id = len(city_data_manager.get_all()) + 1
    city = City(city_id=city_id, name=name)
    city_data_manager.save(city)
    
    return jsonify({
        "id": city.city_id,
        "name": city.name,
        "created_at": city.created_at,
        "updated_at": city.updated_at,
    }), 201

@app.route("/cities", methods=["GET"])
def list_cities():
    cities = city_data_manager.get_all()
    cities_list = [{
        "id": city.city_id,
        "name": city.name,
        "created_at": city.created_at,
        "updated_at": city.updated_at,
    } for city in cities]
    
    return jsonify(cities_list), 200

@app.route("/cities/<int:city_id>", methods=["GET"])
def get_city(city_id):
    city = city_data_manager.get(city_id)
    if not city:
        abort(404, "City not found.")
    
    return jsonify({
        "id": city.city_id,
        "name": city.name,
        "created_at": city.created_at,
        "updated_at": city.updated_at,
    }), 200

@app.route("/cities/<int:city_id>", methods=["PUT"])
def update_city(city_id):
    city = city_data_manager.get(city_id)
    if not city:
        abort(404, "City not found.")
    
    data = request.get_json()
    if not data or "name" not in data:
        abort(400, "Missing required fields.")
    
    name = data["name"]
    if not name:
        abort(400, "Name cannot be empty.")
    
    city.name = name
    city_data_manager.update(city)
    
    return jsonify({
        "id": city.city_id,
        "name": city.name,
        "created_at": city.created_at,
        "updated_at": city.updated_at,
    }), 200

@app.route("/cities/<int:city_id>", methods=["DELETE"])
def delete_city(city_id):
    city = city_data_manager.get(city_id)
    if not city:
        abort(404, "City not found.")
    
    city_data_manager.delete(city_id)
    return '', 204

if __name__ == "__main__":
    app.run(debug=True)