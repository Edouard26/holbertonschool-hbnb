class Country:
    def __init__(self, name, country_code):
        self.name = name
        self.country_code = country_code
        self.cities = []

    def add_city(self, city):
        self.cities.append(city)
        city.counry = self

    def __repr__(self):
        return f"Country(name={self.name}, country_code={self.country_code})"
