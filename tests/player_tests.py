import unittest
import sys

sys.path.insert(0, "/home/ayaqdop/base")

from player import Player

class PlayerTest(unittest.TestCase):

    def test_init(self):
        team = "Test Team"
        number = 42
        target = Player(team, number)

        self.assertEqual(team, target.team)
        self.assertEqual(number, target.number)

    def test_init_false(self):
        team = "Test Team"
        number = 42
        target = Player(team, number)

        self.assertEqual("Test Team", target.team)
        self.assertNotEqual("42", target.number)


if __name__ == '__main__':
    unittest.main()