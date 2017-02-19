import unittest
import sys

sys.path.insert(0, "/home/ayaqdop/base")

from ball import Ball

class BallTest(unittest.TestCase):

    def test_init(self):
        target = Ball()
        self.assertIsInstance(target.possible_moves, list)

    def test_str(self):
        target = Ball()
        self.assertEqual("@", str(target))
