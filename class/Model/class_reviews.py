#!/user/bin/python3


class reviews:
    places_id:int
    users_id:int
    text:str
    rating:str


    def __init__(self, data:dict):
        self.text = data["text"]
        self.rating = data["rating"]
        self.places_id = data["places_id"]
        self.users_id = data["users_id"]


    def __repr__(self):
        return (f"reviews {self.text}, {self.rating}")
