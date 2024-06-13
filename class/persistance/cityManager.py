#!/user/bin/python3

from DataManager import DataManager
from ..Models.City import City

class CityManager(DataManager):
    """
    City Manager.
    """
    cloud_database = "cities.json"
    cloud_entity_class = City
    cloud_primary_key = "id"

    def __init__(self):
        self.cloud_PATH = self.cloud_database
        super().__init__()

    def getCity(self, city_id: int) -> (City | None):
        return self.get(city_id)

    def createCity(self, name: str, country_id: str) -> City:
        city_data = {
            "name": name,
            "country_id": country_id
        }
        return self.save(city_data)

    def updateCity(self, city_id: int, name: str = None, country_id: str = None) -> bool:
        city = self.getCity(city_id)
        if city is None:
            return False

        if name is not None:
            city.name = name
        if country_id is not None:
            city.country_id = country_id

        self.update(city.__dict__)
        return True

    def deleteCity(self, city_id: int) -> bool:
        return self.delete(city_id)
