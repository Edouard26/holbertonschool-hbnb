from base_model import basemodel

class reviews(basemodel):
    def __init__(self, user_id, rating):
        super().__init__(uuid4, name, created_at, updated_at)
    self.user_id = ID
    self.rating = rating
