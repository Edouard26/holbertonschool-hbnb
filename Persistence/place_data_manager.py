from ipersistence_manager import IPersistenceManager

class PlaceDataManager(IPersistenceManager):
    def __init__(self):
        self.place = {}

    def save(self, place):
        place_id = place.get_id()
        self.place[place_id] = place
        print(f"Saved Place with ID {place_id}")

    def get(self, place_id):
        return self.place.get(place_id, None)

    def update(self, place):
        place_id = place.get_id()
        if place_id in self.place:
            self.place[place_id] = place
            print(f"Updated Place with ID {place_id}")
        else:
            print(f"Place with ID {place_id} does not exist")

    def delete(self, place_id):
        if place_id in self.place:
            del self.place[place_id]
            print(f"Deleted Place with ID {place_id}")
        else:
            print(f"Place with ID {place_id} does not exist")