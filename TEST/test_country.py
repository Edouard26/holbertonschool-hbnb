import unittest
from class_country import Country
class TestCountry(unittest.TestCase):
    def test_country_initialization(self):
        country = Country("France", "FR")
        self.assertEqual(country.name, "France")
        self.assertEqual(country.country_code, "FR")

if __name__ == "__main__":
    unittest.main()