from ipersistence_manager import IPersistenceManager

class CountryDataManager(IPersistenceManager):
    def __init__(self):
        self.countries = {}

    def save(self, country):
        country_id = country.get_id()
        self.countries[country_id] = country
        print(f"Saved Country with ID {country_id}")

    def get(self, country_id):
        return self.countries.get(country_id, None)

    def update(self, country):
        country_id = country.get_id()
        if country_id in self.countries:
            self.countries[country_id] = country
            print(f"Updated Country with ID {country_id}")
        else:
            print(f"Country with ID {country_id} does not exist")

    def delete(self, country_id):
        if country_id in self.countries:
            del self.countries[country_id]
            print(f"Deleted Country with ID {country_id}")
        else:
            print(f"Country with ID {country_id} does not exist")