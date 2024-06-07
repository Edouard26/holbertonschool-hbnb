from class-Amenities import Amenities
from class-Places import Places

# Création des instances de Amenities
wifi = Amenities(1, "Wi-Fi")
pool = Amenities(2, "Swimming Pool")

# Ajout des commodités au lieu
wifi.add_amenity(wifi)
pool.add_amenity(pool)

# Vérification des relations
print(wifi.amenities)
print(pool.amenities)
