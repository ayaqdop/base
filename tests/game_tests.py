import unittest
import sys

sys.path.insert(0, "/home/ayaqdop/base")

from game import Game
from ball import Ball
from field import Field

class GameTest(unittest.TestCase):

    def test_init(self):
        player1 = "Quanysh"
        player2 = "Olzhas"
        target = Game(player1, player2)

        self.assertEqual(0, target.time_limit)
        self.assertEqual(0, target.score_limit)
        self.assertIsNone(target.turn)
        self.assertIsNone(target.teams)
        self.assertIsInstance(target.ball, Ball)
        self.assertIsInstance(target.field, Field)
