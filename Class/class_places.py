class places:
    def __init__(self, area, gps, nb_of_rooms, max_guest):
        self.area = area
        self.gps = gps
        self.nb_of_rooms = nb_of_rooms
        self.max_guest = max_guest
        self.Cities = City
        self.amenities = []
        city.places.append(self)


    def details(self):
        print(f"Area: {self.area} m²")
        print(f"GPS coordinates: {self.gps}")
        print(f"Number of rooms: {self.nb_of_rooms}")
        print(f"Number max of guests: {self.max_guest}")

    def add_amenity(self, amenity):
        self.amenities.append(amenity)

class Appartment(places):
    def __init__(self, area, gps, nb_of_rooms, max_guest):
        super().__init__(area, gps, nb_of_rooms, max_guest)
    
    def details(self):
        print("Type: appartment")
        super().details()

class House(places):
    def __init__(self, area, gps, nb_of_rooms, max_guest):
        super().__init__(area, gps, nb_of_rooms, max_guest)

    def details(self):
        print("Type: house")
        super().details()

class Room(places):
    def __init__(self, area, gps, max_guest):
        super().__init__(area, gps, 1, max_guest)

    def details(self):
        print("Type: room")
        super().details()
