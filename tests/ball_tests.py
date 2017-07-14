from unittest import TestCase
from ball import Ball


class BallTest(TestCase):
    def test_init(self):
        target = Ball()
        self.assertIsInstance(target.possible_moves, list)

    def test_str(self):
        target = Ball()
        self.assertEqual("@", str(target))
