class Reviews:
    def __init__(self, ID, place, user_id, rating, comment):
        self.ID = ID
        self.place = place
        self.user_id = user_id
        self.rating = rating
        self.comment = comment
        place.reviews.append(self)
        user.reviews.append(self)

    def Write_review(self, customer)
    customer.log(f"Review ID {self.ID} started.")
