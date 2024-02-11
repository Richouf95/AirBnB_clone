#!/usr/bin/python3
"""
    Defines unittests for models/amenity.py.
"""


import unittest
from models.amenity import Amenity
from datetime import datetime
from time import sleep
import os


class TestAmenity(unittest.TestCase):

    def test_init_with_name(self):
        """Tests initialization with a name argument."""
        amenity = Amenity()
        self.assertTrue(isinstance(amenity.id, str))
        self.assertIsNotNone(amenity.created_at)
        self.assertEqual(amenity.created_at, amenity.updated_at)

    def test_init_without_name(self):
        """Tests initialization without arguments."""
        amenity = Amenity()
        self.assertEqual("", amenity.name)
        self.assertTrue(isinstance(amenity.id, str))
        self.assertIsNotNone(amenity.created_at)
        self.assertEqual(amenity.created_at, amenity.updated_at)

    def test_to_dict_attributes(self):
        """Tests the inclusion of expected attributes in to_dict()."""
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        expected_keys = {"id", "created_at", "updated_at", "__class__"}
        self.assertSetEqual(set(amenity_dict.keys()), expected_keys)

    def test_to_dict_datetime_format(self):
        """Tests the format of datetime attributes in to_dict()."""
        now = datetime.now()
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertEqual(str, type(amenity_dict["created_at"]))
        self.assertEqual(str, type(amenity_dict["updated_at"]))

    def test_unique_ids(self):
        """Tests if different instances have unique IDs."""
        amenity1 = Amenity()
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.id, amenity2.id)

    def test_updated_at_on_save(self):
        """Tests if updated_at changes after save()."""
        amenity = Amenity()
        original_updated_at = amenity.updated_at
        sleep(0.1)  # Introduce a slight time difference
        amenity.save()
        self.assertGreater(amenity.updated_at, original_updated_at)


if __name__ == "__main__":
    unittest.main()
