from base_model import basemodel

class Amenity(basemodel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_dict(self):
        return super().to_dict()