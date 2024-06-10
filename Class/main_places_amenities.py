from class_amenities import amenities
from class_places import places

# Création des instances de Amenities
wifi = amenities(1, "Wi-Fi")
pool = amenities(2, "Swimming Pool")

# Ajout des commodités au lieu
wifi.add_amenity(wifi)
pool.add_amenity(pool)

# Vérification des relations
print(wifi.amenities)
print(pool.amenities)
