from base_model import basemodel

class places(basemodel):
    def __init__(self, basemodel, area, gps, nb_of_rooms, max_guest):
        super().__init__(uuid4, name, created_at, updated_at)
    self.basemodel
    self.area = area
    self.gps = gps
    self.nb_of_rooms = nb_of_rooms
    self.max_guest = max_guest
       
    class apartment(places):
        def __init__(self, places):
        super().__init__(basemodel, area, gps, nb_of_rooms, max_guest)
    
    class house(places):
        def __init__(self, places):
        super().__init__(basemodel, area, gps, nb_of_rooms, max_guest)

    class room(places):
        def __init__(self, places):
        super().__init__(basemodel, area, gps, 1, max_guest)