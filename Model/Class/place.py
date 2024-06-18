from base_model import BaseModel

class Place(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.area = kwargs.get('area', 0)
        self.gps = kwargs.get('gps', "")
        self.nb_of_rooms = kwargs.get('nb_of_rooms', 0)
        self.max_guest = kwargs.get('max_guest', 0)

    def to_dict(self):
        place_dict = super().to_dict()
        place_dict.update({
            'area': self.area,
            'gps': self.gps,
            'nb_of_rooms': self.nb_of_rooms,
            'max_guest': self.max_guest
        })
        return place_dict


if __name__ == "__main__":
    place = Place(area=100, gps="40.7128,-74.0060", nb_of_rooms=3, max_guest=5)
    print(place.to_dict())
    place.save()
    print(place.to_dict())