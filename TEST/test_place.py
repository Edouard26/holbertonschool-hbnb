import unittest
from datetime import datetime
import time
from class_place import Place, Apartment, House, Room

class City:
    def __init__(self, name, country_code):
        self.name = name
        self.country_code = country_code
        self.places = []

    def add_place(self, place):
        self.places.append(place)

class TestPlace(unittest.TestCase):
    def setUp(self):
        self.city1 = City("Paris", "FR")
        self.city2 = City("Lyon", "FR")
        self.place = Place(120, "48.8566, 2.3522", 3, 4, self.city1)

    def test_initialization(self):
        self.assertEqual(self.place.area, 120)
        self.assertEqual(self.place.gps, "48.8566, 2.3522")
        self.assertEqual(self.place.nb_of_rooms, 3)
        self.assertEqual(self.place.max_guest, 4)
        self.assertEqual(self.place.city, self.city1)
        self.assertIsInstance(self.place.created_at, datetime)
        self.assertIsInstance(self.place.updated_at, datetime)

    def test_update_place(self):
        initial_updated_at = self.place.updated_at
        time.sleep(0.01)  # Assure que le temps a passé
        self.place.update_place(area=150, gps="45.7640, 4.8357", max_guest=6, city=self.city2)
        self.assertEqual(self.place.area, 150)
        self.assertEqual(self.place.gps, "45.7640, 4.8357")
        self.assertEqual(self.place.max_guest, 6)
        self.assertEqual(self.place.city, self.city2)
        self.assertGreater(self.place.updated_at, initial_updated_at)

class TestApartment(unittest.TestCase):
    def setUp(self):
        self.city = City("Paris", "FR")
        self.apartment = Apartment(100, "48.8566, 2.3522", 2, 3, self.city)

    def test_initialization(self):
        self.assertEqual(self.apartment.area, 100)
        self.assertEqual(self.apartment.gps, "48.8566, 2.3522")
        self.assertEqual(self.apartment.nb_of_rooms, 2)
        self.assertEqual(self.apartment.max_guest, 3)
        self.assertEqual(self.apartment.city, self.city)
        self.assertIsInstance(self.apartment.created_at, datetime)
        self.assertIsInstance(self.apartment.updated_at, datetime)

class TestHouse(unittest.TestCase):
    def setUp(self):
        self.city = City("Paris", "FR")
        self.house = House(200, "48.8566, 2.3522", 4, 8, self.city)

    def test_initialization(self):
        self.assertEqual(self.house.area, 200)
        self.assertEqual(self.house.gps, "48.8566, 2.3522")
        self.assertEqual(self.house.nb_of_rooms, 4)
        self.assertEqual(self.house.max_guest, 8)
        self.assertEqual(self.house.city, self.city)
        self.assertIsInstance(self.house.created_at, datetime)
        self.assertIsInstance(self.house.updated_at, datetime)

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.city = City("Paris", "FR")
        self.room = Room(20, "48.8566, 2.3522", 1, self.city)

    def test_initialization(self):
        self.assertEqual(self.room.area, 20)
        self.assertEqual(self.room.gps, "48.8566, 2.3522")
        self.assertEqual(self.room.nb_of_rooms, 1)
        self.assertEqual(self.room.max_guest, 1)
        self.assertEqual(self.room.city, self.city)
        self.assertIsInstance(self.room.created_at, datetime)
        self.assertIsInstance(self.room.updated_at, datetime)

if __name__ == '__main__':
    unittest.main()
