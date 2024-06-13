class country(basemodel):
    def __init__(self, basemodel, name, country_code):
        super().__init__(id, name, created_at, updated_at)
        self.basemodel
        self.name = name
        self.country_code = country_code
        self.city = city
