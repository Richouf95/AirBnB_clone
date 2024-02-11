#!/usr/bin/python3
"""
    Defines unittests for models/city.py.
"""


import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test unitaire pour la classe City"""

    def test_instanciation(self):
        """Test l'instanciation d'une ville"""
        ville = City()
        self.assertIsInstance(ville, City)
        self.assertEqual(ville.name, "")
        self.assertEqual(ville.state_id, "")

    def test_str(self):
        """Test la représentation textuelle d'une ville"""
        ville = City()
        ville_str = str(ville)
        self.assertIn("[City]", ville_str)
        self.assertIn("id", ville_str)
        self.assertIn("created_at", ville_str)

    def test_to_dict(self):
        """Test la conversion d'une ville en dictionnaire"""
        ville = City()
        ville_dict = ville.to_dict()
        self.assertIsInstance(ville_dict, dict)
        self.assertIn("id", ville_dict)
        self.assertIn("created_at", ville_dict)
        self.assertIn("updated_at", ville_dict)

    def test_save(self):
        """Test la sauvegarde d'une ville"""
        ville = City(name="Marseille", state_id="FR-PACA")
        ville.save()


if __name__ == "__main__":
    unittest.main()
