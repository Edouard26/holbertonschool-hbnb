class places:
    def __init__(self, basemodel, area, gps, nb_of_rooms, max_guest, amenities, city):
        self.basemodel
        self.area = area
        self.gps = gps
        self.nb_of_rooms = nb_of_rooms
        self.max_guest = max_guest
        self.city = city
        city.places.append(self)
        self.amenities = amenities


    def details(self):
        print(f"Area: {self.area} m²")
        print(f"GPS coordinates: {self.gps}")
        print(f"Number of rooms: {self.nb_of_rooms}")
        print(f"Number max of guests: {self.max_guest}")

    def add_amenity(self, amenity):
        self.amenities.append(amenity)

class apartment(places):
    def __init__(self, area, gps, nb_of_rooms, max_guest, amenities, city):
        super().__init__(area, gps, nb_of_rooms, max_guest, amenities, city)
    
    def details(self):
        print("Type: appartment")
        super().details()

class house(places):
    def __init__(self, area, gps, nb_of_rooms, max_guest, amenities, city):
        super().__init__(area, gps, nb_of_rooms, max_guest, amenities, city)

    def details(self):
        print("Type: house")
        super().details()

class room(places):
    def __init__(self, area, gps, max_guest, amenities, city):
        super().__init__(area, gps, 1, max_guest, amenities, city)

    def details(self):
        print("Type: room")
        super().details()
