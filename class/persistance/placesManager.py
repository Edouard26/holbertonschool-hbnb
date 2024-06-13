from .DataManager import DataManager
from ..Models.Place import Place

class PlaceManager(DataManager):
    """
    Place Manager.
    """
    cloud_database = "places.json"
    cloud_entity_class = Place
    cloud_primary_key = "id"

    def __init__(self):
        self.cloud_PATH = self.cloud_database
        super().__init__()

    def getPlace(self, place_id: int) -> (Place | None):
        return self.get(place_id)

    def createPlace(self, user_id: str, name: str, description: str, number_rooms: int, number_bathrooms: int, max_guest: int, price_by_night: int, latitude: float, longitude: float) -> Place:
        place_data = {
            "user_id": user_id,
            "name": name,
            "description": description,
            "number_rooms": number_rooms,
            "number_bathrooms": number_bathrooms,
            "max_guest": max_guest,
            "price_by_night": price_by_night,
            "latitude": latitude,
            "longitude": longitude
        }
        return self.save(place_data)

    def updatePlace(self, place_id: int, **kwargs) -> bool:
        place = self.getPlace(place_id)
        if place is None:
            return False

        for key, value in kwargs.items():
            if hasattr(place, key):
                setattr(place, key, value)

        self.update(place.__dict__)
        return True

    def deletePlace(self, place_id: int) -> bool:
        return self.delete(place_id)
