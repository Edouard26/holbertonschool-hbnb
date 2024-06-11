class Review:
    def __init__(self, ID, place, user, rating, comment):
        self.ID = ID
        self.place = place
        self.user = user
        self.rating = rating
        self.comment = comment
        place.add_review(self)
        user.reviews.append(self)
