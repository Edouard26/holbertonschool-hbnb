class city:
    def __init__(self, ID, name, country_code, country, places):
        self.ID = ID
        self.name = name
        self.country_code = country_code
        self.country = country
        country.city.append(self)
