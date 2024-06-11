from flask import Flask, request, jsonify
import uuid
from datetime import datetime

app = Flask(__name__)

# Exemple de données en mémoire (à remplacer par une base de données ou un système de fichiers)
reviews = []

class User:
    def __init__(self, username, ID, password, email, first_name, last_name, age):
        self.username = username
        self.ID = ID
        self.password = password
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.reviews = []

class Place:
    def __init__(self, ID, name, city):
        self.ID = ID
        self.name = name
        self.city = city
        self.reviews = []
    
    def add_review(self, review):
        self.reviews.append(review)

class Review:
    def __init__(self, ID, place, user, rating, comment):
        self.ID = ID
        self.place = place
        self.user = user
        self.rating = rating
        self.comment = comment
        place.add_review(self)
        user.reviews.append(self)

# Routes pour gérer les avis

@app.route('/reviews', methods=['POST'])
def create_review():
    data = request.json
    ID = str(uuid.uuid4())
    place = Place(data['place_id'], data['place_name'], data['place_city'])
    user = User(data['username'], data['user_id'], data['password'], data['email'], data['first_name'], data['last_name'], data['age'])
    rating = data['rating']
    comment = data['comment']
    
    review = Review(ID, place, user, rating, comment)
    reviews.append(review)
    
    return jsonify({'id': ID, 'place': place.name, 'user': user.username, 'rating': rating, 'comment': comment}), 201

@app.route('/reviews', methods=['GET'])
def get_reviews():
    reviews_list = [
        {
            'id': review.ID,
            'place': review.place.name,
            'user': review.user.username,
            'rating': review.rating,
            'comment': review.comment
        } for review in reviews
    ]
    return jsonify(reviews_list), 200

@app.route('/reviews/<review_id>', methods=['GET'])
def get_review(review_id):
    review = next((r for r in reviews if r.ID == review_id), None)
    if review is None:
        return jsonify({'error': 'Review not found'}), 404
    
    review_data = {
        'id': review.ID,
        'place': review.place.name,
        'user': review.user.username,
        'rating': review.rating,
        'comment': review.comment
    }
    return jsonify(review_data), 200

@app.route('/reviews/<review_id>', methods=['PUT'])
def update_review(review_id):
    review = next((r for r in reviews if r.ID == review_id), None)
    if review is None:
        return jsonify({'error': 'Review not found'}), 404
    
    data = request.json
    review.rating = data.get('rating', review.rating)
    review.comment = data.get('comment', review.comment)
    
    return jsonify({'id': review.ID, 'place': review.place.name, 'user': review.user.username, 'rating': review.rating, 'comment': review.comment}), 200

@app.route('/reviews/<review_id>', methods=['DELETE'])
def delete_review(review_id):
    global reviews
    reviews = [r for r in reviews if r.ID != review_id]
    
    return jsonify({'message': 'Review deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)
