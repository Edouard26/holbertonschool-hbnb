class Place:
    def __init__(self, area, gps, nb_of_rooms, max_guest, cities):
        self.area = area
        self.gps = gps
        self.nb_of_rooms = nb_of_rooms
        self.max_guest = max_guest
        self.cities = cities
        self.amenities = []
        cities.add_place(self)
    
    def add_review(self, review):
        self.reviews.append(review)
        
    def details(self):
        print(f"Area: {self.area} m²")
        print(f"GPS coordinates: {self.gps}")
        print(f"Number of rooms: {self.nb_of_rooms}")
        print(f"Maximum number of guests: {self.max_guest}")

    def add_amenity(self, amenity):
        self.amenities.append(amenity)

class Apartment(Place):
    def __init__(self, area, gps, nb_of_rooms, max_guest, city):
        super().__init__(area, gps, nb_of_rooms, max_guest, city)

    def details(self):
        print("Type: Apartment")
        super().details()

class House(Place):
    def __init__(self, area, gps, nb_of_rooms, max_guest, city):
        super().__init__(area, gps, nb_of_rooms, max_guest, city)

    def details(self):
        print("Type: House")
        super().details()

class Room(Place):
    def __init__(self, area, gps, max_guest, city):
        super().__init__(area, gps, 1, max_guest, city)

    def details(self):
        print("Type: Room")
        super().details()
