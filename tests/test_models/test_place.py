#!/usr/bin/python3
"""Defines unittests for models/place.py.

Unittest classes:
    TestPlace_instantiation
    TestPlace_save
    TestPlace_to_dict
"""


import os
import unittest
from datetime import datetime
import models
from models.place import Place


class TestPlaceCreation(unittest.TestCase):
    """Tests the instantiation of the Place class."""

    def test_instantiation_without_arguments(self):
        """Verifies that a Place instance can be created without arguments."""
        place = Place()
        self.assertIsInstance(place, Place)

    def test_storage_in_global_object(self):
        """Verifies that the new instance is properly stored"""
        place = Place()
        self.assertIn(place, models.storage.all().values())

    def test_id_is_a_public_string(self):
        """Verifies that the `id` attribute is a public string."""
        place = Place()
        self.assertEqual(str, type(place.id))

    def test_created_at_is_a_public_datetime(self):
        """Verifies that the `created_at` attribute is a public `datetime`"""
        place = Place()
        self.assertEqual(datetime, type(place.created_at))

    def test_updated_at_is_a_public_datetime(self):
        """Verifies that the `updated_at` attribute is a public `datetime`"""
        place = Place()
        self.assertEqual(datetime, type(place.updated_at))

    def test_two_places_have_unique_ids(self):
        """Verifies that two Place instances have unique IDs."""
        place1 = Place()
        place2 = Place()
        self.assertNotEqual(place1.id, place2.id)


if __name__ == "__main__":
    unittest.main()
