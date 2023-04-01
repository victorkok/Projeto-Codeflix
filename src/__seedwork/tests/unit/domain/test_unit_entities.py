
from abc import ABC
from dataclasses import is_dataclass
import unittest

from __seedwork.domain.entities import Entity
from __seedwork.domain.value_objects import ValueObject


class TestEntityUnit(unittest.TestCase):

    def test_if_is_a_datacass(self):
        self.assertTrue(is_dataclass(Entity))

    def test_if_is_a_abstract_class(self):
        self.assertIsInstance(Entity(), ABC)