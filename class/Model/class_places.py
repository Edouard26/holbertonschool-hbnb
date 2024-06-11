#!/user/bin/python3


class places:
    
    id: int
    name: str
    adress: str
    number_rooms: int
    number_bathrooms: int
    price_by_night: int
    max_guests: int
    amenities: list
    users_id:int
    city_id:int


    def __init__(self, data:dict)
        self.name = data["name"]
        self.number_room = data["number_room"]
        self.number_bithroom = data["number_bithroom"]
        self.max_guest = data["max_guest"]
        self.price_by_night = data["price_by_night"]
        self.city_id = data["city"]
        self.Amennities_id = data["Amenities_id"]
        self.users_id = data["users"]
        self.id = data["id"]
