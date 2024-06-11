from flask import Flask, request, jsonify
from class_country import Country  # Assurez-vous d'importer correctement votre classe

app = Flask(__name__)

# Dictionnaire pour stocker les pays
countries = {}

@app.route('/countries', methods=['POST'])
def create_country():
    data = request.get_json()
    name = data.get('name')
    country_code = data.get('country_code')
    if not name or not country_code:
        return jsonify({'error': 'Invalid input'}), 400

    country = Country(name, country_code)
    countries[country.country_code] = country
    return jsonify({
        'name': country.name,
        'country_code': country.country_code,
        'cities': country.cities
    }), 201

@app.route('/countries/<country_code>', methods=['GET'])
def get_country(country_code):
    country = countries.get(country_code)
    if not country:
        return jsonify({'error': 'Country not found'}), 404

    return jsonify({
        'name': country.name,
        'country_code': country.country_code,
        'cities': country.cities
    })

@app.route('/countries/<country_code>', methods=['PUT'])
def update_country(country_code):
    country = countries.get(country_code)
    if not country:
        return jsonify({'error': 'Country not found'}), 404

    data = request.get_json()
    country.name = data.get('name', country.name)
    country.country_code = data.get('country_code', country.country_code)
    return jsonify({
        'name': country.name,
        'country_code': country.country_code,
        'cities': country.cities
    })

@app.route('/countries/<country_code>', methods=['DELETE'])
def delete_country(country_code):
    country = countries.pop(country_code, None)
    if not country:
        return jsonify({'error': 'Country not found'}), 404

    return jsonify({'message': 'Country deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
