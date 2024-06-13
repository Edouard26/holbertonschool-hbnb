#!/usr/bin/python3

from .ModelBase import ModelBase

class user(ModelBase):
    def __init__(self, ID, email, first_name, last_name, username, password):
        self.ID = ID
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password


    def to_dict(self):
        return {

                "email": self.email,
                "first_name": self.first_name,
                "last_name": self.last_name,
                "username": self.username,
                "password": self.password,
                "ID": self.ID,
    }

    def __str__(self) -> str:
        return (f"[user] {self.ID} , {self.username}")
