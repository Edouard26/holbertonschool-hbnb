from class_city import city
from class_country import country
from class_places import places, apartment, house

# Création des instances de Country et City
france = country("France", "FR")
paris = city(1, "Paris", france)

# Création des instances de Place et ses sous-classes
apartment_in_paris = apartment(75, "48.8566 N, 2.3522 E", 3, 5, paris)
house_in_paris = house(250, "48.8566 N, 2.3522 E", 6, 10, paris)

# Affichage des détails
apartment_in_paris.details()
house_in_paris.details()
