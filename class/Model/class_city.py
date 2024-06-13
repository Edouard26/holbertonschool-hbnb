#!/user/bin/python3

from .ModelBase import ModelBase

class city(ModelBase):

    def __init__(self, name, created_at, updated_at, country_code, ID)
        self.name = name
        self.country_code = country_code
        self.id = ID
        self.created_at = created_at
        self.updated_at = updated_at

    def tojson(self):
        return {
                "ID": self.ID,
                "name": self.name,
                "country_code": self.country_code,
                "created_at": self.created_at,
                "updated_at": self.updated_at,
            }   
        
    def __str__(self) -> str:
        return f"[City] {self.ID} , {self.name} , {self.country_code}"
