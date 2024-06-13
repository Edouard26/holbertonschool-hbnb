from base_model import basemodel

class amenities(basemodel):
    def __init__(self):
        super().__init__(uuid4, name, created_at, updated_at)
