from flask import Flask, request, jsonify, abort
from country_data_manager import CountryDataManager
from Model.Class.country import Country

app = Flask(__name__)
country_data_manager = CountryDataManager()

@app.route("/countries", methods=["POST"])
def create_country():
    data = request.get_json()
    if not data or "name" not in data:
        abort(400, "Missing required fields.")
    
    name = data["name"]
    if not name:
        abort(400, "Name cannot be empty.")
    
    country_id = len(country_data_manager.get_all()) + 1
    country = Country(country_id=country_id, name=name)
    country_data_manager.save(country)
    
    return jsonify({
        "id": country.country_id,
        "name": country.name,
        "created_at": country.created_at,
        "updated_at": country.updated_at,
    }), 201

@app.route("/countries", methods=["GET"])
def list_countries():
    countries = country_data_manager.get_all()
    countries_list = [{
        "id": country.country_id,
        "name": country.name,
        "created_at": country.created_at,
        "updated_at": country.updated_at,
    } for country in countries]
    
    return jsonify(countries_list), 200

@app.route("/countries/<int:country_id>", methods=["GET"])
def get_country(country_id):
    country = country_data_manager.get(country_id)
    if not country:
        abort(404, "Country not found.")
    
    return jsonify({
        "id": country.country_id,
        "name": country.name,
        "created_at": country.created_at,
        "updated_at": country.updated_at,
    }), 200

@app.route("/countries/<int:country_id>", methods=["PUT"])
def update_country(country_id):
    country = country_data_manager.get(country_id)
    if not country:
        abort(404, "Country not found.")
    
    data = request.get_json()
    if not data or "name" not in data:
        abort(400, "Missing required fields.")
    
    name = data["name"]
    if not name:
        abort(400, "Name cannot be empty.")
    
    country.name = name
    country_data_manager.update(country)
    
    return jsonify({
        "id": country.country_id,
        "name": country.name,
        "created_at": country.created_at,
        "updated_at": country.updated_at,
    }), 200

@app.route("/countries/<int:country_id>", methods=["DELETE"])
def delete_country(country_id):
    country = country_data_manager.get(country_id)
    if not country:
        abort(404, "Country not found.")
    
    country_data_manager.delete(country_id)
    return '', 204

if __name__ == "__main__":
    app.run(debug=True)