#!/usr/bin/python3


import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):

    def test_init_with_kwargs(self):
        """Teste l'initialisation avec des kwargs."""
        now = datetime.now()
        new_model = BaseModel(
                id="1234",
                created_at=now.isoformat(),
                updated_at=now.isoformat()
                )
        self.assertEqual(new_model.id, "1234")
        self.assertEqual(new_model.created_at, now)
        self.assertEqual(new_model.updated_at, now)

    def test_init_without_kwargs(self):
        """Teste l'initialisation sans kwargs."""
        new_model = BaseModel()
        self.assertTrue(isinstance(new_model.id, str))
        self.assertIsNotNone(new_model.created_at)
        self.assertEqual(new_model.created_at, new_model.updated_at)

    def test_save(self):
        """Teste la méthode save."""
        now = datetime.now()
        new_model = BaseModel()
        old_updated_at = new_model.updated_at
        new_model.save()
        self.assertNotEqual(old_updated_at, new_model.updated_at)
        self.assertGreater(new_model.updated_at, now)

    def test_to_dict(self):
        """Teste la méthode to_dict."""
        new_model = BaseModel()
        new_dict = new_model.to_dict()
        expected_dict = {
            "id": new_model.id,
            "created_at": new_model.created_at.isoformat(),
            "updated_at": new_model.updated_at.isoformat(),
            "__class__": "BaseModel",
        }
        self.assertEqual(new_dict, expected_dict)

    def test_str(self):
        """Teste la méthode __str__."""
        new_model = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(
                new_model.id,
                new_model.__dict__
                )
        self.assertEqual(str(new_model), expected_str)


if __name__ == '__main__':
    unittest.main()
