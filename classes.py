class Places:
    def __init__(self, area, gps, nb_of_rooms, max_guest):
        self.area = area
        self.gps = gps
        self.nb_of_rooms = nb_of_rooms
        self.max_guest = max_guest

    def details(self):
        print(f"Area: {self.area} m²")
        print(f"GPS coordinates: {self.gps}")
        print(f"Number of rooms: {self.nb_of_rooms}")
        print(f"Number max of guests: {self.max_guest}")

class Appartment(Places):
    def __init__(self, area, gps, nb_of_rooms, max_guest):
        super().__init__(area, gps, nb_of_rooms, max_guest)
    
    def details(self):
        print("Type: Appartment")
        super().details()

class House(Places):
    def __init__(self, area, gps, nb_of_rooms, max_guest):
        super().__init__(area, gps, nb_of_rooms, max_guest)

    def details(self):
        print("Type: House")
        super().details()

class Room(Places):
    def __init__(self, area, gps, max_guest):
        super().__init__(area, gps, 1, max_guest)

    def details(self):
        print("Type: Room")
        super().details()
