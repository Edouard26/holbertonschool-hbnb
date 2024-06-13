from datetime import datetime
class Review:
    def __init__(self, ID, place, user, rating, comment):
        self.ID = ID
        self.place = place
        self.user = user
        self.rating = rating
        self.comment = comment
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        place.add_review(self)
        user.reviews.append(self)
        
    def update_review(self, new_rating=None, new_comment=None):
        if new_rating is not None:
            self.rating = new_rating
        if new_comment is not None:
            self.comment = new_comment
        self.updated_at = datetime.now()