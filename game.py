from ball import Ball
from team import Team
from field import Field

class Game:

    def __init__(self):
        self.time_limit = 0
        self.score_limit = 0
        self.turn = None
        self.ball = Ball()
        self.team = None
        self.field = Field()
