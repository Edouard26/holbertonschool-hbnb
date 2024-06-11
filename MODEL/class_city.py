class city:
    def __init__(self, ID, name, country_code):
        self.ID = ID
        self.name = name
        self.country_code = country_code
        self.places = []
        
    def add_place(self, place):
        """
         Ajoute un lieu à la liste des lieux associés à cette ville.
        
        Args:
            place: Le lieu à ajouter.
        """
        self.places.append(place)