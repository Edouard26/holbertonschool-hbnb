from base_model import basemodel

class country(basemodel):
    def __init__(self, country_code):
        super().__init__(uuid4, name, created_at, updated_at)

    self.country_code = country_code