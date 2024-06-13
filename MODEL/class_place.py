from datetime import datetime

class Place:
    def __init__(self, area, gps, nb_of_rooms, max_guest, city):
        self.area = area
        self.gps = gps
        self.nb_of_rooms = nb_of_rooms
        self.max_guest = max_guest
        self.city = city
        self.amenities = []
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        city.add_place(self)

    def update_place(self, area=None, gps=None, nb_of_rooms=None, max_guest=None, city=None):
        if area is not None:
            self.area = area
        if gps is not None:
            self.gps = gps
        if nb_of_rooms is not None:
            self.nb_of_rooms = nb_of_rooms
        if max_guest is not None:
            self.max_guest = max_guest
        if city is not None:
            self.city = city
        self.updated_at = datetime.now()

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
