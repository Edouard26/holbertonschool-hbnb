#!/usr/bin/python3

from .ModelBase import ModelBase

class amenity(ModelBase):
    def __init__(self, ID, created_at, updated_at, name, text):
    self.name = name
    self.text = text
    self.ID = ID
    self.created_at = created_at
    self.updated_at = updated_at

    def tojson(self):
        return {
                "name": self.name,
                "texte": self.text,
                "created_at": self.created_at,
                "ID": self.ID,
                "updated_at": self.updated_at,
            }
    def __str__(self) -> str:
        return f"[amenity] {self.ID} , {self.name}"
