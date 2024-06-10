import unittest

class TestRealEstateSystem(unittest.TestCase):

    def test_country_city_relationship(self):
        france = Country("France", "FR")
        paris = City(1, "Paris", france)
        self.assertIn(paris, france.cities)
        self.assertEqual(paris.country, france)
    
    def test_city_place_relationship(self):
        france = Country("France", "FR")
        paris = City(1, "Paris", france)
        apartment = Apartment(75, "48.8566 N, 2.3522 E", 3, 5, paris)
        house = House(250, "48.8566 N, 2.3522 E", 6, 10, paris)
        self.assertIn(apartment, paris.places)
        self.assertIn(house, paris.places)
    
    def test_place_details(self):
        france = Country("France", "FR")
        paris = City(1, "Paris", france)
        apartment = Apartment(75, "48.8566 N, 2.3522 E", 3, 5, paris)
        house = House(250, "48.8566 N, 2.3522 E", 6, 10, paris)
        self.assertEqual(apartment.city, paris)
        self.assertEqual(house.city, paris)
        self.assertEqual(paris.country, france)

if __name__ == '__main__':
    unittest.main()
