import unittest
import sys

sys.path.insert(0, "/home/ayaqdop/base")

from field import Field

class FieldTest(unittest.TestCase):

    def test_init(self):
        field = []
        target = Field()
        
        self.assertEqual(field, target.field)