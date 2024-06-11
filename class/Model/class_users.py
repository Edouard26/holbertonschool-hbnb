#!/usr/bin/python3


class users:
    id: int
    username: str
    password: str
    first_name: str
    last_name: str
    email: str


    def __init__(self,  data:dict):
            self.email = data["email"]
            self.first_name = data["first_name"]
            self.last_name = data["last_name"]
            self.username = data["username"]
            self.password = data["password"]
            self.id = data["id"

    def __repr__(self):
        return (f"users {self.email}, {self.first_name}, {self.last_name}")]
