import unittest
import sys

sys.path.insert(0, "/home/ayaqdop/base")

from field import Field

class FieldTest(unittest.TestCase):

    def test_init(self):
        target = Field()
        self.assertIsInstance(target.field, list)