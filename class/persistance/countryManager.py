from DataManager import DataManager
from ..Models.Country import Country

class CountryManager(DataManager):
    """
    Country Manager.
    """
    cloud_database = "countries.json"
    cloud_entity_class = Country
    cloud_primary_key = "id"

    def __init__(self):
        self.cloud_PATH = self.cloud_database
        super().__init__()

    def getCountry(self, country_id: int) -> (Country | None):
        return self.get(country_id)

    def createCountry(self, name: str) -> Country:
        country_data = {
            "name": name
        }
        return self.save(country_data)

    def updateCountry(self, country_id: int, name: str = None) -> bool:
        country = self.getCountry(country_id)
        if country is None:
            return False

        if name is not None:
            country.name = name

        self.update(country.__dict__)
        return True

    def deleteCountry(self, country_id: int) -> bool:
        return self.delete(country_id)
