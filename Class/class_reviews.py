class reviews(basemodel):
    def __init__(self, basemodel, ID, place, user_id, rating, comment):
        super().__init__(id, name, created_at, updated_at)
        self.basemodel
        self.ID = ID
        self.place = place
        self.user_id = user_id
        self.rating = rating
        self.comment = comment
        place.reviews.append(self)
        user.reviews.append(self)

    def write_review(self, customer)
    customer.log(f"Review ID {self.ID} started.")
