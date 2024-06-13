#!/usr/bin/python3

from .ModelBase import ModelBase

class country(ModelBase):

    def __init__(self, name, country_code):
        self.name = name
        self.country_code = country_code

    def tojson(self):
        return {
                "name": self.name,
                "country_code": self.country_code,
            }
    def __str__(self):
        return f"[Country] {self.country_code} , {self.name}"
