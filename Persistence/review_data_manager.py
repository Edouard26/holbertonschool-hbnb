from ipersistence_manager import IPersistenceManager

class ReviewDataManager(IPersistenceManager):
    def __init__(self):
        self.reviews = {}

    def save(self, review):
        review_id = review.get_id()
        self.reviews[review_id] = review
        print(f"Saved Review with ID {review_id}")

    def get(self, review_id):
        return self.reviews.get(review_id, None)

    def update(self, review):
        review_id = review.get_id()
        if review_id in self.reviews:
            self.reviews[review_id] = review
            print(f"Updated Review with ID {review_id}")
        else:
            print(f"Review with ID {review_id} does not exist")

    def delete(self, review_id):
        if review_id in self.reviews:
            del self.reviews[review_id]
            print(f"Deleted Review with ID {review_id}")
        else:
            print(f"Review with ID {review_id} does not exist")