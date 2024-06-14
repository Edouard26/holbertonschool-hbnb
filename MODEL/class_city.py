from base_model import basemodel

class City(basemodel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.city_code = kwargs.get('city_code', "")

    def to_dict(self):
        city_dict = super().to_dict()
        city_dict.update({'city_code': self.city_code})
        return city_dict