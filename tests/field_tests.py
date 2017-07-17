from unittest import TestCase
from field import Field


class FieldTest(TestCase):
    def test_init(self):
        target = Field()
        self.assertIsInstance(target.field, list)
