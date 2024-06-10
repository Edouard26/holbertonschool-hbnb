class cities:
    def __init__(self, ID, name, country_code, country):
        self.ID = ID
        self.name = name
        self.country_code = country_code
        self.country = country
        self.places = []
        country.cities.append(self)
