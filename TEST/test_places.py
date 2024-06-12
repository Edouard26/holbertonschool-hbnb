import unittest
from class_places import Place, Apartment, House, Room
from class_city import city
class TestPlace(unittest.TestCase):
    def setUp(self):
        # Créer des instances de City pour les tests
        self.city1 = city("1", "Paris", "FR")
        self.city2 = city("2", "New York", "US")

    def test_place_initialization(self):
        place = Place(100, (48.8566, 2.3522), 3, 6, self.city1)
        self.assertEqual(place.area, 100)
        self.assertEqual(place.gps, (48.8566, 2.3522))
        self.assertEqual(place.nb_of_rooms, 3)
        self.assertEqual(place.max_guest, 6)
        self.assertEqual(place.city, self.city1)

    def test_apartment_initialization(self):
        apartment = Apartment(80, (40.7128, -74.0060), 2, 4, self.city2)
        self.assertEqual(apartment.area, 80)
        self.assertEqual(apartment.gps, (40.7128, -74.0060))
        self.assertEqual(apartment.nb_of_rooms, 2)
        self.assertEqual(apartment.max_guest, 4)
        self.assertEqual(apartment.city, self.city2)

    def test_house_initialization(self):
        house = House(150, (34.0522, -118.2437), 4, 8, self.city1)
        self.assertEqual(house.area, 150)
        self.assertEqual(house.gps, (34.0522, -118.2437))
        self.assertEqual(house.nb_of_rooms, 4)
        self.assertEqual(house.max_guest, 8)
        self.assertEqual(house.city, self.city1)

    def test_room_initialization(self):
        room = Room(30, (51.5074, -0.1278), 2, self.city2)
        self.assertEqual(room.area, 30)
        self.assertEqual(room.gps, (51.5074, -0.1278))
        self.assertEqual(room.nb_of_rooms, 1)
        self.assertEqual(room.max_guest, 2)
        self.assertEqual(room.city, self.city2)

if __name__ == "__main__":
    unittest.main()
