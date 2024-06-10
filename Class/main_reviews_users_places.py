
from class_reviews import reviews
from class_users import customers
from class_places import places

# Création des instances
john = Customer("john_doe", 101, "securepassword", "john@example.com", "John", "Doe", 30, "CUST123")
review1 = Review(1, appartment_in_paris, john, 5, "Amazing experience!")

# Vérification des relations
print(f"Les critiques écrites par {john.username} : {[review.comment for review in john.reviews]}")
print(f"Les critiques pour {appartment_in_paris.gps} : {[review.comment for review in appartment_in_paris.reviews]}")
