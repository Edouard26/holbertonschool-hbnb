class Place:
    def __init__(self, area, gps, nb_of_rooms, max_guest, city):
        self.area = area
        self.gps = gps
        self.nb_of_rooms = nb_of_rooms
        self.max_guest = max_guest
        self.city = city
        self.amenities = []
        city.add_place(self)

class Apartment(Place):
    def __init__(self, area, gps, nb_of_rooms, max_guest, city):
        super().__init__(area, gps, nb_of_rooms, max_guest, city)
        self.city = city

    def details(self):
        print("Type: Apartment")
        super().details()

class House(Place):
    def __init__(self, area, gps, nb_of_rooms, max_guest, city):
        super().__init__(area, gps, nb_of_rooms, max_guest, city)
        self.city = city

    def details(self):
        print("Type: House")
        super().details()

class Room(Place):
    def __init__(self, area, gps, max_guest, city):
        super().__init__(area, gps, 1, max_guest, city)
        self.city = city

    def details(self):
        print("Type: Room")
        super().details()
