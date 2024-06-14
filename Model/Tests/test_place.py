import json
import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Class.places import Place

class TestPlace(unittest.TestCase):
    def setUp(self):

        self.place1 = Place(area=100, gps="40.7128,-74.0060", nb_of_rooms=3, max_guest=5)
        self.place2 = Place(area=50, gps="34.0522,-118.2437", nb_of_rooms=2, max_guest=3)
        self.place3 = Place(area=75, gps="41.8781,-87.6298", nb_of_rooms=4, max_guest=6)

    def test_initialization(self):

        self.assertEqual(self.place1.area, 100)
        self.assertEqual(self.place1.gps, "40.7128,-74.0060")
        self.assertEqual(self.place1.nb_of_rooms, 3)
        self.assertEqual(self.place1.max_guest, 5)

    def test_to_dict(self):

        place_dict = self.place1.to_dict()
        self.assertEqual(place_dict['area'], 100)
        self.assertEqual(place_dict['gps'], "40.7128,-74.0060")
        self.assertEqual(place_dict['nb_of_rooms'], 3)
        self.assertEqual(place_dict['max_guest'], 5)

    def test_json_serialization(self):

        place1_json = json.dumps(self.place1.to_dict())
        place_dict = json.loads(place1_json)
        self.assertEqual(place_dict['area'], 100)
        self.assertEqual(place_dict['gps'], "40.7128,-74.0060")
        self.assertEqual(place_dict['nb_of_rooms'], 3)
        self.assertEqual(place_dict['max_guest'], 5)

if __name__ == "__main__":
    unittest.main()