from ipersistence_manager import IPersistenceManager

class CityDataManager(IPersistenceManager):
    def __init__(self):
        self.cities = {}

    def save(self, city):
        city_id = city.get_id()
        self.cities[city_id] = city
        print(f"Saved City with ID {city_id}")

    def get(self, city_id):
        return self.cities.get(city_id, None)

    def update(self, city):
        city_id = city.get_id()
        if city_id in self.cities:
            self.cities[city_id] = city
            print(f"Updated City with ID {city_id}")
        else:
            print(f"City with ID {city_id} does not exist")

    def delete(self, city_id):
        if city_id in self.cities:
            del self.cities[city_id]
            print(f"Deleted City with ID {city_id}")
        else:
            print(f"City with ID {city_id} does not exist")