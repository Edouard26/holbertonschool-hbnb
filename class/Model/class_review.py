#!/user/bin/python3

from .ModelBase import ModelBase

class review(ModelBase):
    def __init__(self, ID, text, rating, created_at, updated_at, user_id, place_id):
    
        self.place_id = place_id
        self.user_id = user_id
        self.text = text
        self.rating = rating
        self.ID = ID
        self.created_at = created_at
        self.updated = updated_at


    def tojson(self):
        return {
                "text": self.text,
                "rating": self.rating,
                "places_id": self.place_id,
                "users_id": self.user_id,
                "ID": self.ID,
                "created_at": self.created_at,
                "updated_at": self.created_at,
            }

    def __str__(self) -> str:
            return f"[review] {self.ID} , {self.text}
