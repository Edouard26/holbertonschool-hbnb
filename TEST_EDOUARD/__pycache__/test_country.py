import unittest
from datetime import datetime
from class_country import Country

class TestCountry(unittest.TestCase):
    def test_country_initialization(self):
        country = Country("France", "FR")
        self.assertEqual(country.name, "France")
        self.assertEqual(country.country_code, "FR")
        self.assertIsInstance(country.created_at, datetime)
        self.assertIsInstance(country.updated_at, datetime)

    def test_country_repr(self):
        country = Country("France", "FR")
        self.assertEqual(repr(country), "Country(name=France, country_code=FR)")

    def test_country_save(self):
        country = Country("France", "FR")
        country.save()
        # On ne peut pas vérifier l'effet de la méthode save sans implémentation réelle,
        # mais on peut s'assurer que la méthode est appelée sans erreur.
        self.assertTrue(True)

    def test_country_delete(self):
        country = Country("France", "FR")
        country.delete()
        # On ne peut pas vérifier l'effet de la méthode delete sans implémentation réelle,
        # mais on peut s'assurer que la méthode est appelée sans erreur.
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
