from dataclasses import is_dataclass
from datetime import datetime
import unittest
from category.domain.entities import Category

class TestCategoryUnit(unittest.TestCase):

    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(Category))

    def test_Constructor(self):
        category = Category(
            name='Movie', 
            description='some description', 
            is_active=True,
            created_at= datetime.now()
        )
        self.assertEqual(category.name, 'Movie')
        self.assertEqual(category.description, 'some description')
        self.assertEqual(category.is_active, True)
        self.assertIsInstance(category.created_at, datetime)