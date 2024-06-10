from class_cities import cities
from class_countries import countries
from class_places import places, appartment, house

# Création des instances de Country et City
france = country("France", "FR")
paris = city(1, "Paris", france)

# Création des instances de Place et ses sous-classes
apartment_in_paris = Apartment(75, "48.8566 N, 2.3522 E", 3, 5, paris)
house_in_paris = House(250, "48.8566 N, 2.3522 E", 6, 10, paris)

# Affichage des détails
apartment_in_paris.details()
house_in_paris.details()

# Vérification des relations
print(paris.places)  # Liste des lieux à Paris
print(france.cities)  # Liste des villes en France
