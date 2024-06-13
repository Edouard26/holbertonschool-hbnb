from base_model import basemodel

class city(basemodel):
    def __init__(self, city_code):
        super().__init__(uuid4, name, created_at, updated_at)
    
    self.city_code = city_code