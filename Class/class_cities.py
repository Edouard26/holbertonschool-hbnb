class Cities:
    def __init__(self, ID, name, country_code, country):
        self.ID = ID
        self.name = name
        self.country_code = country_code
        self.country = country
        self.Places = []
        country.cities.append(self)
