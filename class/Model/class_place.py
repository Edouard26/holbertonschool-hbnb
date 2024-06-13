#!/user/bin/python3

from .ModelBase import ModelBase

class place(ModelBase):
    def __init__(self, name, Appartment, max_guest, ID, house, rooms, num_of_rooms, gps, host_id, city_id, price):
    
    self.ID = ID
    self.Appartment = Appartement
    self.name = name
    self.rooms = rooms
    self.num_of_rooms = num_of_rooms
    self.price = price
    self.max_guest = max_guests
    self.house = house
    self.host_id = user_id
    self.city_id = city_id
    self.gps = gps


    def to_dict(self):
        return {

                "Appartment": self.Appartment,
                "name": self.name,
                "gps": self.gps,
                "rooms": self.number_room,
                "num_of_rooms": self.num_of_rooms,
                "max_guest": self.max_guest,
                "price": self.price,
                "city_id": self.city_id,
                "house": self.house,
                "host_id": self.user_id,
                "ID" = self.ID,
    }
    
    def __str__(self) -> str:
        return f"[Place] {self.ID} , {self.name}"
