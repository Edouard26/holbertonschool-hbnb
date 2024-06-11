#!/user/bin/python3


class city:
    name:str
    country:str
    id:int


    def __init__(self, data: dict):
        self.name = data["name"]
        self.country = data["country"]
        self.id = data["id"]



        def __str__(self):
        return (f"[City] {self.id} / {self.country} / {self.name}")

