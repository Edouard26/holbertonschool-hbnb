from base_model import basemodel

class Country(basemodel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.country_code = kwargs.get('country_code', "")

    def to_dict(self):
        country_dict = super().to_dict()
        country_dict.update({'country_code': self.country_code})
        return country_dict
