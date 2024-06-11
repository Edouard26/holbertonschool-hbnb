#!/usr/bin/python3


class Amenities:
    name:int
    text:str


    def __init__(self, name, text):
        self.name = name
        self.texte = text
        
        return (f"(Amenities) {self.name}")
