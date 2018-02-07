from ball import Ball
from team import Team
from field import Field

class Game:

    def __init__(self, player1, player2, team1, team2):
        self.time_limit = 0
        self.score_limit = 0
        self.turn = None
        self.ball = Ball()
        self.teams = None
        self.field = Field()

    def move(self, move_from, move_to):
        pass
