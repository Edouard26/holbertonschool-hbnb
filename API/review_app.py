from flask import Flask, request, jsonify, abort
from review_data_manager import ReviewDataManager
from Model.Class.review import Review

app = Flask(__name__)
review_data_manager = ReviewDataManager()

@app.route("/reviews", methods=["POST"])
def create_review():
    data = request.get_json()
    if not data or "content" not in data:
        abort(400, "Missing required fields.")
    
    content = data["content"]
    if not content:
        abort(400, "Content cannot be empty.")
    
    review_id = len(review_data_manager.get_all()) + 1
    review = Review(review_id=review_id, content=content)
    review_data_manager.save(review)
    
    return jsonify({
        "id": review.review_id,
        "content": review.content,
        "created_at": review.created_at,
        "updated_at": review.updated_at,
    }), 201

@app.route("/reviews", methods=["GET"])
def list_reviews():
    review = review_data_manager.get_all()
    review_list = [{
        "id": review.review_id,
        "content": review.content,
        "created_at": review.created_at,
        "updated_at": review.updated_at,
    } for review in review]
    
    return jsonify(reviews_list), 200

@app.route("/reviews/<int:review_id>", methods=["GET"])
def get_review(review_id):
    review = review_data_manager.get(review_id)
    if not review:
        abort(404, "Review not found.")
    
    return jsonify({
        "id": review.review_id,
        "content": review.content,
        "created_at": review.created_at,
        "updated_at": review.updated_at,
    }), 200

@app.route("/reviews/<int:review_id>", methods=["PUT"])
def update_review(review_id):
    review = review_data_manager.get(review_id)
    if not review:
        abort(404, "Review not found.")
    
    data = request.get_json()
    if not data or "content" not in data:
        abort(400, "Missing required fields.")
    
    content = data["content"]
    if not content:
        abort(400, "Content cannot be empty.")
    
    review.content = content
    review_data_manager.update(review)
    
    return jsonify({
        "id": review.review_id,
        "content": review.content,
        "created_at": review.created_at,
        "updated_at": review.updated_at,
    }), 200

@app.route("/reviews/<int:review_id>", methods=["DELETE"])
def delete_review(review_id):
    review = review_data_manager.get(review_id)
    if not review:
        abort(404, "Review not found.")
    
    review_data_manager.delete(review_id)
    return '', 204

if __name__ == "__main__":
    app.run(debug=True)