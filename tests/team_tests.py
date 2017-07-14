from unittest import TestCase
from team import Team


class TeamTest(TestCase):
    def test_init(self):
        name = "Real Madrid"
        formation = "4-4-2"
        players = []
        target = Team(name, formation, players)

        self.assertEqual(name, target.name)
        self.assertEqual(formation, target.formation)
        self.assertEqual(players, target.players)

    def test_score(self):
        target = Team("Barcelona", "3-5-2", [])
        self.assertEqual(0, target.score)

        target.score += 2
        self.assertEqual(2, target.score)
