class city(basemodel):
    def __init__(self, basemodel, country_code, country, places):
        super().__init__(id, name, created_at, updated_at)
        self.basemodel
        self.ID = ID
        self.name = name
        self.country_code = country_code
        self.country = country
        country.append(self)
