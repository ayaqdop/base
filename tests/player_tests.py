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
        self.assertEqual(Player.MOVES_LEFT, target.moves_left)

    def test_init_false(self):
        team = "Test Team"
        number = 42
        target = Player(team, number)

        self.assertEqual("Test Team", target.team)
        self.assertNotEqual("42", target.number)

    def test_moves_left(self):
        target = Player("Test Team", 42)
        self.assertEqual(Player.MOVES_LEFT, target.moves_left)

        target.moves_left -= 1
        self.assertEqual(2, target.moves_left)

        target.moves_left = 5
        self.assertEqual(5, target.moves_left)
